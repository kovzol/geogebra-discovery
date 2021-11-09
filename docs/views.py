import json
import hashlib
import time
import re
import html.entities
from datetime import datetime, timedelta

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as logina
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.db.models.functions import Length
from django.db.models import Count
from django.db.models import F
from . models import Locale, Category, Translation, Property, TranslationView, GGUser
from . validate import validate_translation, ValidationError
from . normalize import normalize_translation



def JsonResponse(obj):
    return HttpResponse(json.dumps(obj), content_type="application/json")

def get_property_list(props=None, category=None, versions=None, aliases=None):
    prop_filter = {}
    if category:
        if isinstance(category, Category):
            prop_filter["category"] = category
        elif isinstance(category, basestring):
            prop_filter["category__name"] = category
        else:
            raise TypeError
    if versions:
        prop_filter["version__in"] = versions
    if props is None:
        props = Property.objects.filter(**prop_filter)
    prop_list = []
    for prop in props:
        prop_list.append(prop)
        prop_list.append(prop.parent)
        if aliases is not None:
            aliases[prop] = aliases.get(prop, []) + [prop]
            aliases[prop.parent] = aliases.get(prop.parent, []) + [prop]
    return prop_list

def stitch_translations(locales, props=None, category=None, versions=None):
    aliases = {}
    prop_list = get_property_list(props, category, versions, aliases)

    trans_map = {}
    filter_args = {"locale__in": locales}
    filter_args["property__in"] = prop_list
    for trans in Translation.objects.select_related("property").filter(**filter_args).order_by("locale"):
        end_props = aliases.get(trans.property) or [trans.property]
        prev = trans_map.get(end_props[0])
        parent = None
        for prop in end_props:
            if not prop.parent_id:
                parent = prop
            trans_map[prop] = trans
        if prev is None:
            trans.uptodate = True
        else:
            try:
                trans.uptodate = prev.modification_date <= trans.modification_date and ((parent is None) or parent.modification_date <= trans.modification_date)
            except TypeError:
                print("Ooops! Something is wrong with date comparison")
                trans.uptodate = False
    return trans_map

def get_translations(locale, props=None, category=None, fallback=True):
    if fallback:
        ancestry = locale.ancestry()
    else:
        ancestry = [locale]
    return stitch_translations(ancestry, props, category)

def get_translation(prop, locale):
    trans_map = get_translations(locale, props=[prop], fallback=True)
    return trans_map.get(prop, None)

def create_translation_views(reflocale, locale, props=None):
    if isinstance(props, Category):
        trans_cat, trans_props = props, None
        props = Property.objects.filter(category=props)
    else:
        trans_cat, trans_props = None, props
    now = datetime.now()
    m = hashlib.md5((u"%s$foobar" % time.time()).encode('utf-8'))
    view_token = m.hexdigest()
    reftransmap = get_translations(reflocale, trans_props, trans_cat, fallback=True)
    transmap = get_translations(locale, trans_props, trans_cat, fallback=True)
    view = TranslationView.objects.create(
        token=view_token,
        locale=locale,
        reflocale=reflocale,
        property=None,
        view_date=now
    )
    if hasattr(props, "select_related"):
        props = props.select_related()
    for prop in props:
        trans = transmap.get(prop, None)
        reftrans = reftransmap.get(prop, None)
        yield {
            'view_id': view.id,
            'view_key': "%s-%s-%s" % (view.id, view_token, prop.id),
            'key': prop.key,
            'version': prop.version,
            'parent': prop.parent and prop.parent.key,
            'parent_cat': prop.parent and prop.parent.category.name,
            'ref': reftrans,
            'trans': trans and escape_translation(trans.text),
            'hastrans': trans and trans.locale == locale,
            'uptodate': trans and trans.uptodate,
            'category': prop.category.name,
            'key_comment': prop.comment,
            'comment': trans and trans.comment or "",
            'max_length': prop.max_length
        }

def decorate_translation_view(view):
    if view['category'] == 'command':
        key = view['key']
        i = key.find(".")
        if i != -1:
            key = key[:i]
        view['wikilink'] = "/wiki.php?command=%s" % key
    return view

def delete_old_views():
    one_day_ago = datetime.now() - timedelta(1)
    #TranslationView.objects.filter(view_date__lt=one_day_ago).delete()

def confirm(request):
    if request.method == 'GET':
        raise Http404
    user_container = dict()
    authenticate(request=request, user_container=user_container)
    gguser = GGUser.objects.get(tube_id=user_container.get('gguserid', -1))
    gguser.copyright = datetime.now()
    gguser.save()
    return HttpResponseRedirect("/ggbtrans/props/ggauth/")

def ggauth(request):
    return view_translations(request)

def ggauth_admin(request):
    user_container = dict()
    user = authenticate(request=request, user_container=user_container)
    if user is not None:
        if user.is_active:
            logina(request, user)
            return HttpResponseRedirect("/ggbtrans/admin")
    return view_translations(request)

def missing_badge(request, user_container):
    return render(request, "properties/message.html",
                  {'gguserpic': user_container.get('gguserpic', None), 'ggusername' : user_container.get('ggusername', None),
                   'message':'You are not currently assigned to any translation team. Please sign in with a a different account or contact <a href="mailto:transaltion@geogebra.org">translation@geogebra.org</a> if you want to join.'})

def status(request):
    user_container = dict()
    authenticate(request=request, user_container=user_container)
    if request.GET.get('report', None) == "length":
        return status_length(request, user_container)
    loc_id = request.GET.get('loc', None)
    if loc_id:
        return status_loc(request, user_container, loc_id)
    start = time.time()
    english = Locale.objects.get(description="Default")
    keys = []
    data = []
    defaults = dict()
    cat_bundles = [["menu", "error", "colors"], ["command"], ["website", "website-services"], ["tube", "navigation", "wiki"], ["install"]]
    cat_bundle_titles = ["Apps", "Commands", "Homepage", "Groups + Editor", "App Stores"]
    totals = dict()
    for bundle in cat_bundles:
        bundle_ids = []
        for prop in Property.objects.filter(category__name__in=bundle, version__in=["stable", "beta"], parent__isnull=True):
            bundle_ids = bundle_ids + [prop.parent_id if prop.parent else prop.id]
        totals[",".join(bundle)] = bundle_ids
    for trans in Translation.objects.filter(property__category__name="links", locale=english):
        keys = keys + [trans.property.key]
        defaults[trans.property.key] = trans.text
    header = cat_bundle_titles + keys
    for locale in Locale.objects.exclude(language="en").order_by('description'):
        tutorials = dict()
        row = []
        for bundle in cat_bundles:
            pct = Translation.objects.filter(locale=locale, property_id__in=totals[",".join(bundle)]).count()  *100.0 / len(totals[",".join(bundle)])
            row = row + [dict(pct=int(pct), classname=("green" if pct >= 80 else "yellow"))]
        for trans in Translation.objects.filter(property__category__name="links", locale=locale):
            if locale.description == 'Default' or trans.text != defaults[trans.property.key]:
                tutorials[trans.property.key] = trans.text
        for key in keys:
            row = row + [dict(id=tutorials.get(key, None), key=key, classname="default")]
        data = data + [dict(head=locale.description, cells=row, link="?loc=%s" % locale.id)]
    return render(request, "properties/status.html",
                  {'gguserpic': user_container.get('gguserpic', None), 'ggusername' : user_container.get('ggusername', None),
                   'data': data, 'header': header, 'duration': (time.time()-start)})

def status_loc(request, user_container, loc_id):
    data = []
    header = ["translations"]
    translation_set = Translation.objects.filter(locale__id=loc_id) if int(loc_id) > 0 else Translation.objects.all()
    user_map = dict()
    for gguser in GGUser.objects.all():
        user_map[gguser.user_id] = gguser.tube_id
    trans_count = translation_set.values('author__username', 'author__id').annotate(total=Count('author__username')).order_by('-total')
    for trans in trans_count:
        link = "https://mat.geogebra.org/user/profile/id/%s" % user_map.get(trans["author__id"], "?")
        data = data + [dict(head=trans["author__username"], link=link, cells=[dict(pct=trans["total"])])]
    return render(request, "properties/status.html",
                  {'gguserpic': user_container.get('gguserpic', None), 'ggusername' : user_container.get('ggusername', None),
                   'data': data, 'header': header, 'duration': 0})

def status_length(request, user_container):
    data = []
    header = ["translations"]
    limited_props = Property.objects.filter(max_length__gt=1)
    for prop in limited_props:
        translation_set = Translation.objects.annotate(text_len=Length('text')).filter(property=prop, text_len__gt=prop.max_length)
        for trans in translation_set:
            link = "../../admin/properties/translation/%s/change/" % trans.pk
            data = data + [dict(head=trans.property.key + " / " + trans.locale.description, link=link, cells=[dict(pct=len(trans.text))])]
    return render(request, "properties/status.html",
                  {'gguserpic': user_container.get('gguserpic', None), 'ggusername' : user_container.get('ggusername', None),
                   'data': data, 'header': header, 'duration': 0})

def check_login(request, user):
    if user is not None:
        if user.is_active:
            logina(request, user)
    else:
        logout(request)

def as_dict(arr, key_name, coeff=1):
    missing = dict()
    for propcount in arr:
        missing[propcount.get(key_name, 0)] = coeff * propcount.get('id__count', 0)
    return missing

structure = [dict(id="GUI", cats=[1, 3, 5]), dict(id="Commands", cats=[2]),
             dict(id="Website", cats=[6, 9, 10, 12]), dict(id="Install", cats=[11, 22]),
             dict(id="Resource IDs", cats=[15]), dict(id="Moodle", cats=[14, 16, 17]), dict(id="Forum", cats=[18, 19, 20])]

def make_groups(parts, key_name):
    for heading in structure:
        heading[key_name] = 0
        heading["cat_link"] = ",".join([str(s) for s in heading["cats"]])
        for part in parts:
            for cat in heading["cats"]:
                heading[key_name] += part.get(cat, 0)

def make_headings(locale):
    propcounts = Property.objects.filter(version__in=['stable', 'beta']).filter(parent__isnull=True).values("category").annotate(Count("id")).order_by()
    to_translate = as_dict(propcounts, 'category')
    beta_translation = Translation.objects.filter(locale=locale).filter(property__version__in=['stable', 'beta'])
    transcounts = beta_translation.values("property__category").annotate(Count("id")).order_by()
    translated = as_dict(transcounts, 'property__category', -1)
    make_groups([to_translate, translated], "missing")
    obsolete_count = beta_translation.filter(property__modification_date__gte=F("modification_date")).values("property__category").annotate(Count("id")).order_by()
    obsolete = as_dict(obsolete_count, 'property__category')
    make_groups([to_translate, translated, obsolete], "obsolete")
    return structure

def view_translations(request):
    user_container = dict()
    user = authenticate(request=request, user_container=user_container)
    check_login(request, user)
    if not request.user.is_authenticated:
        return render(request, "properties/message.html",
                      {'gguserid': None, 'ggusername' : None,
                       'message' : 'Please sign in to use this system.'})
    badges = user_container.get('badges', [])
    if len(badges) < 1 and not request.user.is_staff:
        return missing_badge(request, user_container)
    if request.user.is_authenticated and user_container.get('copyright', datetime.fromtimestamp(0)) < datetime.fromtimestamp(123456789):
        return render(request, "properties/copyright.html",
                      {'gguserpic': user_container.get('gguserpic', None),
                       'ggusername' : user_container.get('ggusername', None)})
    locales = Locale.objects.extra(select={'desc':"case when description=='Default' then 'Aaa' else description end"}).order_by('desc')
    mylocales = [t for t in locales if t.badge() in badges]
    if request.user.is_staff:
        mylocales = locales
    request.session['badges'] = badges
    loc_id = request.GET.get('loc', None)
    if len(mylocales) < 1:
        return missing_badge(request, user_container)
    if loc_id is not None:
        locale = get_object_or_404(Locale, pk=loc_id)
    else:
        locale = mylocales[0]
    headings = make_headings(locale)
    if request.GET.get('cat', "0") == "0" and request.GET.get('key', "0") == "0" and request.GET.get('search_text', None) is None:
        recent = Translation.objects.filter(locale=locale).filter(property__version__in=["stable", "beta"]).order_by('-modification_date')
        recent = recent[:50]
        recent = [{'text':t.text, 'key':t.property.key, 'date':t.modification_date, 'author':t.author} for t in recent]
        return render(request, "properties/message.html",
                      {'gguserpic': user_container.get('gguserpic', None),
                       'staff': request.user.is_staff, 'ggusername' : user_container.get('ggusername', None),
                       'message':'No category selected. Below you can see recent changes to '+locale.description,
                       'locale':locale, 'beta':True, 'limit':100, 'headings':headings,
                       'recent':recent, 'locale_list':locales, 'user_locales':mylocales})
    return render_translations(request, "properties/translate.html", user_container.get('gguserpic', None), user_container.get('ggusername', None), mylocales, headings)

def render_translations(request, tplname, gguserpic, ggusername, mylocales, headings):
    if request.method == 'POST':
        raise Http404
    delete_old_views()
    loc_id = request.GET.get('loc', None)
    cat_string = request.GET.get('cat', '') or '1,3,5'
    cat_id = cat_string.split(',')
    if request.GET.get('tube', '') != '':
        cat_id = "9"
    ref_id = request.GET.get('ref', 1)
    beta = request.GET.get('beta', False)
    if beta:
        beta = True
    search_text = request.GET.get('search_text', None)
    limit = int(request.GET.get('limit', 100))
    if loc_id is not None:
        locale = get_object_or_404(Locale, pk=loc_id)
    else:
        locale = mylocales[0]
    ref_locale = get_object_or_404(Locale, pk=ref_id)
    category = []
    catnames = []
    for ci in cat_id:
        category.append(get_object_or_404(Category, pk=ci))
        catnames.append(get_object_or_404(Category, pk=ci).name)
    locales = Locale.objects.all().order_by('description')

    user_locales = mylocales

    # We use java native translations for javaui in some languages
    v_beta = ["stable", "beta"]
    #3Author.objects.annotate(average_rating=Avg('book__rating'))
    if search_text:
        found_trans = Translation.objects.filter(
            text__contains=search_text,
            locale__in=[locale, Locale.objects.get(pk=1)],
            property__version__in=v_beta
        ) | Translation.objects.filter(
            comment__contains=search_text,
            locale__in=[locale, Locale.objects.get(pk=1)],
            property__version__in=v_beta
        )
        found_props = Property.objects.filter(
            key__contains=search_text
        ).filter(version__in=v_beta) | Property.objects.filter(
            comment__contains=search_text
        ).filter(version__in=v_beta)
        props = [t.property for t in found_trans] + [p for p in found_props]
    elif request.GET.get('key', '') != '':
        [cat, key] = request.GET.get('key', '').split(":")
        props = Property.objects.filter(category__name=cat).filter(key=key)
    else:
        if beta:
            props = Property.objects.filter(category__in=category).filter(version__in=v_beta)
        else:
            props = Property.objects.filter(
                category__in=category
            ).filter(version="stable")
    if locale in user_locales:
        translations = create_translation_views(ref_locale, locale, props)
        # Removing duplicates (first converting the dict object to hashable)
        translations = [dict(t) for t in set([tuple(d.items()) for d in translations])]
        # Show untranslated properties first
        translations = sorted(
            translations,
            key=lambda t: 2  + (t['uptodate'] * 1) if t['hastrans'] else t['uptodate']
        )
        count = len(translations)
        if limit > 0 and limit < count:
            translations = translations[:limit]
    #else:
    #    return render(request, "properties/message.html",
    #      {'gguserpic': user_container.get('gguserpic',None), 'ggusername' : user_container.get('ggusername',None),
    #  'message':'You are not currently assigned to this translation team. Please sign in with a a different account or contact <a href="mailto:transaltion@geogebra.org">translation@geogebra.org</a> if you want to join.'},
    locales = [l for l in locales if l.description]

    response = render(request, tplname, {
        'locale': locale,
        'reflocale': ref_locale,
        'category': category,
        'beta': beta,
        'locale_list': locales,
        'headings': headings,
        'cat_string': cat_string,
        'translation_list': map(decorate_translation_view, translations),
        'request': request,
        'cookie': request.COOKIES.get("SSID"),
        'user_locales': user_locales,
        'search_term': search_text,
        'gguserpic': gguserpic,
        'ggusername': ggusername,
        'staff': request.user.is_staff,
        'count':count,
        'limit':limit,
        'tube': request.GET.get('tube', ''),
        'tube_cookie': request.GET.get('tube_cookie', None) == 'true' or (request.COOKIES.get("ggbtranstube") and  request.GET.get('tube_cookie', None) != 'false'),
        'badges':""
    })
    update_tube_cookie(request, response)
    return response

def update_tube_cookie(request, response):
    if request.GET.get('tube_cookie', None) == 'true':
        response.set_cookie('ggbtranstube', '1', domain='.geogebra.org')
    if  request.GET.get('tube_cookie', None) == 'false':
        response.set_cookie('ggbtranstube', '1', domain='.geogebra.org', expires=datetime.strftime(datetime.utcnow() + timedelta(seconds=-10), "%a, %d-%b-%Y %H:%M:%S GMT"))


# Inspired from http://effbot.org/zone/re-sub.htm#unescape-html

escape_translation_ptn = re.compile(u"[\u200e\u200f]")

def escape_translation(text):
    def fixup(m):
        code = ord(m.group(0))
        try:
            name = html.entities.codepoint2name[code]
            return u"{{%s}}" % name
        except KeyError:
            return u"{{#x%04x}}" % code
    return escape_translation_ptn.sub(fixup, text)

def unescape_translation(text):
    text = text.strip().replace('\r\n', '\n')
    def fixup(m):
        text = m.group(1)
        bits = text.split()
        chars = []
        for bit in bits:
            if bit.startswith('#'):
                try:
                    if bit.startswith('#x'):
                        chars.append(unichr(int(bit[2:], 16)))
                    else:
                        chars.append(unichr(int(bit[1:])))
                except ValueError:
                    pass
            else:
                # named entity
                try:
                    chars.append(unichr(html.entities.name2codepoint[bit]))
                except KeyError:
                    pass
        return u"".join(chars)
    return re.sub("{{(.*?)}}", fixup, text)

def validate_update(request):
    if request.method != 'POST' or not request.user.is_authenticated:
        return None
    view_key = request.POST['view_key']
    view_id, token, prop_id = view_key.split("-")
    try:
        prop = Property.objects.get(pk=prop_id)
    except Property.DoesNotExist:
        return None
    try:
        view = TranslationView.objects.get(
            #pk=view_id,
            token=token,
            property=prop
        )
    except TranslationView.DoesNotExist:
        try:
            gen_view = TranslationView.objects.get(
                pk=view_id,
                token=token,
                property=None
            )
            view = TranslationView(
                #pk=view_id,
                token=token,
                property=prop,
                locale=gen_view.locale,
                reflocale=gen_view.reflocale,
                view_date=gen_view.view_date
            )
        except TranslationView.DoesNotExist:
            return None
    return view

def list_properties(request):
    translations = Translation.objects.filter(text=request.GET['translation'], locale__id=1)
    res = []
    for trans in translations:
        res = res + [{"id":trans.property.pk, "key": trans.property.category.name +"::"+trans.property.key}]
    return JsonResponse(res)

def update_translation(request):
    view = validate_update(request)
    if view is None:
        return JsonResponse({"result": "error"})
    prop = view.property
    locale = view.locale
    response = {}
    if (locale.badge() not in request.session.get('badges', [])) and (not request.user.is_staff):
        return JsonResponse({"result": "error"})
    # prop = view.property
    text = unescape_translation(request.POST['text'])
    if prop.max_length is not None and length(text) > prop.max_length and prop.max_length > 0:
        return JsonResponse({"result": "error", "message": "too long"})
    trans = get_translation(prop, locale)
    translation_modified = False
    if trans is None or trans.locale != locale:
        # There is no translation in this locale: create one
        trans = Translation(
            locale=locale,
            property=prop,
            text=text
        )
        translation_modified = True
    elif trans.modification_date > view.view_date:
        # Another view updated this translation after this view
        # was obtained and before this update was requested
        response['result'] = 'error'
        response['message'] = 'translation update conflict'
        return JsonResponse(response)
    elif text != trans.text:
        trans.text = text
        translation_modified = True
    elif not trans.uptodate:
        translation_modified = True
    try:
        validate_translation(trans)
    except ValidationError as e:
        response['result'] = 'error'
        response['message'] = "\n".join(e.args[0])
    else:
        response['result'] = 'success'
        if translation_modified:
            trans.author = request.user
            normalize_translation(trans)
            trans.save()
            view.view_date = trans.modification_date
            view.save()
            response['text'] = escape_translation(trans.text)
    return JsonResponse(response)

def reset_translation(request):
    if request.method != "GET" or not request.user.is_authenticated:
        return JsonResponse({'result': 'error'})
    view_key = request.GET['view_key']
    view_id, token, prop_id = view_key.split("-")
    try:
        prop = Property.objects.get(pk=prop_id)
    except Property.DoesNotExist:
        return JsonResponse({"result": "error"})
    try:
        gen_view = TranslationView.objects.get(
            pk=view_id,
            token=token,
            property=None
        )
    except TranslationView.DoesNotExist:
        return JsonResponse({"result": "error"})
    trans = get_translation(prop, gen_view.reflocale) or ""
    return JsonResponse({
        'result': 'success',
        'default': escape_translation(trans.text)
    })

def update_comment(request):
    if request.method != "POST" or not request.user.is_authenticated:
        return JsonResponse({'result': 'error'})
    comment_text = request.POST.get('text', '').strip()
    view_key = request.POST['view_key']
    view_id, token, prop_id = view_key.split("-")
    try:
        prop = Property.objects.get(pk=prop_id)
    except Property.DoesNotExist:
        return JsonResponse({"result": "error"})
    try:
        gen_view = TranslationView.objects.get(
            pk=view_id,
            token=token,
            property=None
        )
    except TranslationView.DoesNotExist:
        return JsonResponse({"result": "error"})
    try:
        trans = Translation.objects.get(
            property=prop,
            locale=gen_view.locale
        )
    except Translation.DoesNotExist:
        return JsonResponse({'result': 'error'})
    trans.comment = comment_text or None
    trans.save()
    return JsonResponse({
        'result': 'success',
        'text': comment_text
    })

def import_batch(request):
    title = 'OK'
    rows = request.POST.get('props', '').split('\n')
    res = ''
    for row in rows:
        idx = row.find('=')
        rhs = row[idx+1:]
        lhs = row[:idx]
        res = res + ',' + lhs + ',' + rhs
        try:
            prop = Property.objects.get(key=lhs, category=Category.objects.get(name='helpdesk'))
        except Property.DoesNotExist:
            prop = Property(key=lhs, category=Category.objects.get(name='helpdesk'), version='test')
            prop.save()
        try:
            trans = Translation.objects.filter(property=prop).get(locale=Locale.objects.get(pk=1))
            trans.text = rhs
        except Translation.DoesNotExist:
            trans = Translation(
                locale=Locale.objects.get(pk=1),
                property=prop,
                text=rhs,
                author=User.objects.get(pk=1)
                )
        trans.save()
    return render(request, "properties/import_batch.html", {
        'title': title,
        'res': res
        })

def import_help(request):
    import xml.etree.ElementTree as ET
    title = 'OK'
    e = ET.fromstring(request.POST.get('props', '<language><info/><translations/></language>').encode('utf-8'))
    res = ''
    if e[1]:
        for row in e[1].findall('translation'):
            rhs = row.findtext('value')
            lhs = row.findtext('key')
            res = res + ',' + lhs + ',' + rhs
            found = False
            try:
                prop = Property.objects.get(key=lhs, category__in=Category.objects.filter(name__in=['helpdesk', 'helpdeskf', 'helpdeskr']))
                found = True
            except Property.DoesNotExist:
                title = 'Property not found'
            if found:
                try:
                    trans = Translation.objects.filter(property=prop).get(locale=Locale.objects.get(pk=64))
                except Translation.DoesNotExist:
                    trans = Translation(
                        locale=Locale.objects.get(pk=64),
                        property=prop,
                        text=rhs,
                        author=User.objects.get(pk=1)
                        )
                    trans.save()
    return render(request, "properties/import_batch.html", {
        'title': title,
        'res': res
        })

