#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This program adds extra entries in the ggbtrans database.
# These extra entries are not (yet) official properties and translations.
# Currently this program is used to maintain an extended translation database for GeoGebra Discovery,
# see https://github.com/kovzol/geogebra-discovery for details.
# Author: Zoltán Kovács <zoltan@geogebra.org>

# Usage:
# 1. Add entries in the main program (see below, at the end of this file). Don't delete existing entries, just add new ones.
# 2. Copy the raw ggbtransdb file from the current database to this folder.
# 3. Run this program.
# 4. Create an output folder, e.g. output-trunk, with "mkdir output-trunk".
# 5. Run "./export.py trunk output-trunk ggbtransdb".
# 6. Copy the contents of the output-trunk folder to fork/geogebra/common-jre/src/nonfree/resources/org/geogebra/common/jre/properties
#    in your local repository of GeoGebra Discovery.
# 7. Create another output folder, e.g. output-gwtjs, with "mkdir output-gwtjs".
# 8. Run "./export.py gwtjs output-gwtjs ggbtransdb".
# 9. Copy the contents of the output-trunk folder to fork/geogebra/web/src/nonfree/resources/org/geogebra/web/pub/js
#    in your local repository of GeoGebra Discovery.
# 10. Test the new translations.
# 11. Commit the changes in the fork/geogebra/ folder.

# We avoid overwriting or overlapping any existing or future entries, so we start our patching in a large ID area.
start_properties_translation_id = 1000000; # < 360000 on 2021-05-09
start_properties_property_id = 100000; # < 8000 on 2021-05-09

properties_translation_id = start_properties_translation_id
properties_property_id = start_properties_property_id

try:
    import sqlite3
except ImportError:
    import pysqlite2.dbapi2 as sqlite3

import shutil, time, optparse, os.path

def next_property_id():
    global properties_property_id
    properties_property_id += 1
    return properties_property_id

def add_property(properties_property_id, category_id, version, key):
    with sqlite3.connect("ggbtransdb") as conn:
        c = conn.cursor()
        query = "INSERT INTO properties_property (id, parent_id, category_id, version, comment, key, creation_date, modification_date, max_length, ticket) VALUES "
        query += "(" + str(properties_property_id) + ", NULL, " + str(category_id) + ", '" + str(version) + "', "
        query += "'created by a patch via patch.py', " + "'" + key + "', " + "DATE('now'), DATE('now'), NULL, NULL)"
        print(query)
        c.execute(query)

def add_translation(property_id, locale_id, text, author_id):
    with sqlite3.connect("ggbtransdb") as conn:
        c = conn.cursor()
        global properties_translation_id
        properties_translation_id += 1
        query = "INSERT INTO properties_translation (id, property_id, locale_id, text, comment, creation_date, modification_date, author_id) VALUES "
        query += "(" + str(properties_translation_id) + ", " + str(property_id) + ", " + str(locale_id) + ", " + "'" + text + "', "
        query += "'created by a patch via patch.py', DATE('now'), DATE('now'), " + str(author_id) + ")"
        print(query)
        c.execute(query)

def add_command(properties_property_id, key):
    add_property(properties_property_id, 2, 'stable', key)

def add_menu(properties_property_id, key):
    add_property(properties_property_id, 5, 'stable', key)

def cleanup():
    with sqlite3.connect("ggbtransdb") as conn:
        c = conn.cursor()
        global start_properties_translation_id
        query = "DELETE from properties_translation WHERE id > " + str(start_properties_translation_id)
        print(query)
        c.execute(query)
        global start_properties_property_d
        query = "DELETE from properties_property WHERE id > " + str(start_properties_property_id)
        print(query)
        c.execute(query)

if __name__ == "__main__":
    # Delete eventually existing former extra entries:
    cleanup()

    # Create IDs for new properties.

    DISCOVER = next_property_id()
    DISCOVER_SYNTAX = next_property_id()
    DISCOVER_TOOL = next_property_id()
    DISCOVER_TOOL_HELP = next_property_id()
    DISCOVERED_THEOREMS_ON_POINT = next_property_id()
    NO_THEOREMS_FOUND = next_property_id()
    REDRAW_DIFFERENTLY = next_property_id()
    UNSUPPORTED_STEPS = next_property_id()
    IDENTICAL_POINTS_A = next_property_id()
    COLLINEAR_POINTS_A = next_property_id()
    CONCYCLIC_POINTS_A = next_property_id()
    SETS_OF_PARALLEL_AND_PERPENDICULAR_LINES_A = next_property_id()
    CONGRUENT_SEGMENTS_A = next_property_id()
    IN_PROGRESS = next_property_id()
    CANNOT_DECIDE_EQUALITY_OF_POINTS_A_B = next_property_id()

    COMPARE = next_property_id()
    COMPARE_SYNTAX = next_property_id()
    COMPARE_A_AND_B = next_property_id()

    INCIRCLECENTER = next_property_id()
    INCIRCLECENTER_SYNTAX = next_property_id()
    INCIRCLECENTER_TOOL = next_property_id()
    INCIRCLECENTER_TOOL_HELP = next_property_id()

    INCIRCLE_TOOL = next_property_id()
    INCIRCLE_TOOL_HELP = next_property_id()

    LOCUSEQUATION_TOOL = next_property_id()
    LOCUSEQUATION_TOOL_HELP = next_property_id()

    ENVELOPE_TOOL = next_property_id()
    ENVELOPE_TOOL_HELP = next_property_id()

    PROVE_THAT_A = next_property_id()
    LET_A_BE_ARBITRARY_POINTS = next_property_id()
    LET_A_BE_THE_B = next_property_id()
    LET_A_BE_A_B = next_property_id()
    LET_A_BE_THE_REGULAR_POLYGON_BCD = next_property_id()
    LET_A_BE_THE_REGULAR_BGON_VERTICES_C = next_property_id()
    DENOTE_THE_EXPRESSION_A_BY_B = next_property_id()

    REALQUANTIFIERELIMINATION = next_property_id()
    REALQUANTIFIERELIMINATION_SYNTAX = next_property_id()

    # Languages
    EN = 1
    DE = 6
    ES = 9
    HU = 16

    # Authors
    ZK = 34 # Zoltán Kovács

    # Properties
    add_command(DISCOVER, 'Discover')
    add_command(DISCOVER_SYNTAX, 'Discover.Syntax')
    add_menu(DISCOVER_TOOL, 'Discover')
    add_menu(DISCOVER_TOOL_HELP, 'Discover.Help')
    add_menu(DISCOVERED_THEOREMS_ON_POINT, 'DiscoveredTheoremsOnPointA')
    add_menu(NO_THEOREMS_FOUND, 'NoTheoremsFound')
    add_menu(REDRAW_DIFFERENTLY, 'RedrawDifferently')
    add_menu(UNSUPPORTED_STEPS, 'UnsupportedSteps')
    add_menu(CONCYCLIC_POINTS_A, 'ConcyclicPointsA')
    add_menu(IDENTICAL_POINTS_A, 'IdenticalPointsA')
    add_menu(COLLINEAR_POINTS_A, 'CollinearPointsA')
    add_menu(CONGRUENT_SEGMENTS_A, 'CongruentSegmentsA')
    add_menu(SETS_OF_PARALLEL_AND_PERPENDICULAR_LINES_A, 'SetsOfParallelAndPerpendicularLinesA')
    add_menu(IN_PROGRESS, 'InProgress')
    add_menu(CANNOT_DECIDE_EQUALITY_OF_POINTS_A_B, 'CannotDecideEqualityofPointsAB')
    add_translation(DISCOVER, EN, 'Discover', ZK)
    add_translation(DISCOVER, DE, 'Entdecken', ZK)
    add_translation(DISCOVER, ES, 'Descubrir', ZK)
    add_translation(DISCOVER, HU, 'Felfedezés', ZK)
    add_translation(DISCOVER_TOOL, EN, 'Discover', ZK)
    add_translation(DISCOVER_TOOL, DE, 'Entdecken', ZK)
    add_translation(DISCOVER_TOOL, ES, 'Descubrir', ZK)
    add_translation(DISCOVER_TOOL, HU, 'Felfedezés', ZK)
    add_translation(DISCOVER_TOOL_HELP, EN, 'Select one point', ZK)
    add_translation(DISCOVER_TOOL_HELP, HU, 'Egy pont kijelölése', ZK)
    add_translation(DISCOVER_TOOL_HELP, DE, 'Gib einen Punkt an', ZK)
    add_translation(DISCOVER_TOOL_HELP, ES, 'Selecciona punto', ZK)
    add_translation(DISCOVERED_THEOREMS_ON_POINT, EN, 'Discovered theorems on point %0', ZK)
    add_translation(DISCOVERED_THEOREMS_ON_POINT, DE, 'Entdeckungen über den Punkt %0', ZK)
    add_translation(DISCOVERED_THEOREMS_ON_POINT, ES, 'Teoremas descubiertos con el punto %0', ZK)
    add_translation(DISCOVERED_THEOREMS_ON_POINT, HU, 'A(z) %0 ponttal kapcsolatos felfedezések', ZK)
    add_translation(DISCOVER_SYNTAX, EN, '[ <Point> ]', ZK)
    add_translation(DISCOVER_SYNTAX, DE, '[ <Punkt> ]', ZK)
    add_translation(DISCOVER_SYNTAX, HU, '[ <Pont> ]', ZK)
    add_translation(DISCOVER_SYNTAX, ES, '[ <Punto> ]', ZK)
    add_translation(NO_THEOREMS_FOUND, EN, 'No theorems were found.', ZK)
    add_translation(NO_THEOREMS_FOUND, DE, 'Keine Sätze wurden gefunden.', ZK)
    add_translation(NO_THEOREMS_FOUND, HU, 'Nincs semmi figyelemreméltó.', ZK)
    add_translation(NO_THEOREMS_FOUND, ES, 'No se encontraron teoremas descubiertos.', ZK)
    add_translation(REDRAW_DIFFERENTLY, EN, 'Try to redraw the construction differently.', ZK)
    add_translation(REDRAW_DIFFERENTLY, DE, 'Versuchen Sie, die Konstruktion anders zu zeichnen.', ZK)
    add_translation(REDRAW_DIFFERENTLY, HU, 'Próbálja újrarajzolni az ábrát másképpen!', ZK)
    add_translation(REDRAW_DIFFERENTLY, ES, 'Intente volver a dibujar la figura de forma diferente.', ZK)
    add_translation(UNSUPPORTED_STEPS, EN, 'The construction contains unsupported steps.', ZK)
    add_translation(UNSUPPORTED_STEPS, ES, 'La figura consta de pasos no compatibles.', ZK)
    add_translation(UNSUPPORTED_STEPS, DE, 'Die Konstruktion enthält Schritte, die nicht unterstützt sind.', ZK)
    add_translation(UNSUPPORTED_STEPS, HU, 'Nem támogatott lépéseket tartalmaz a szerkesztés.', ZK)
    add_translation(IDENTICAL_POINTS_A, EN, 'Identical points: %0', ZK)
    add_translation(IDENTICAL_POINTS_A, DE, 'Identische Punkte: %0', ZK)
    add_translation(IDENTICAL_POINTS_A, ES, 'Puntos idénticos: %0', ZK)
    add_translation(IDENTICAL_POINTS_A, HU, 'Megegyező pontok: %0', ZK)
    add_translation(COLLINEAR_POINTS_A, EN, 'Collinear points: %0', ZK)
    add_translation(COLLINEAR_POINTS_A, DE, 'Kollineare Punkte: %0', ZK)
    add_translation(COLLINEAR_POINTS_A, ES, 'Puntos colineales: %0', ZK)
    add_translation(COLLINEAR_POINTS_A, HU, 'Kollineáris pontok: %0', ZK)
    add_translation(CONCYCLIC_POINTS_A, EN, 'Concyclic points: %0', ZK)
    add_translation(CONCYCLIC_POINTS_A, DE, 'Konzyklische Punkte: %0', ZK)
    add_translation(CONCYCLIC_POINTS_A, ES, 'Puntos concíclicos: %0', ZK)
    add_translation(CONCYCLIC_POINTS_A, HU, 'Egy körre illeszkedő pontok: %0', ZK)
    add_translation(CONGRUENT_SEGMENTS_A, EN, 'Congruent segments: %0', ZK)
    add_translation(CONGRUENT_SEGMENTS_A, DE, 'Kongruente Strecken: %0', ZK)
    add_translation(CONGRUENT_SEGMENTS_A, ES, 'Segmentos congruentes: %0', ZK)
    add_translation(CONGRUENT_SEGMENTS_A, HU, 'Egybevágó szakaszok: %0', ZK)
    add_translation(SETS_OF_PARALLEL_AND_PERPENDICULAR_LINES_A, EN, 'Sets of parallel and perpendicular lines: %0', ZK)
    add_translation(SETS_OF_PARALLEL_AND_PERPENDICULAR_LINES_A, DE, 'Mengen von parallelen und senkrechten Geraden: %0', ZK)
    add_translation(SETS_OF_PARALLEL_AND_PERPENDICULAR_LINES_A, ES, 'Líneas paralelas y perpendiculares: %0', ZK)
    add_translation(SETS_OF_PARALLEL_AND_PERPENDICULAR_LINES_A, HU, 'Párhuzamos és merőleges egyenesek: %0', ZK)
    add_translation(IN_PROGRESS, EN, 'In progress', ZK)
    add_translation(IN_PROGRESS, DE, 'In Bearbeitung', ZK)
    add_translation(IN_PROGRESS, ES, 'En curso', ZK)
    add_translation(IN_PROGRESS, HU, 'Folyamatban', ZK)
    add_translation(CANNOT_DECIDE_EQUALITY_OF_POINTS_A_B, EN, 'Cannot decide equality of points %0 and %1.', ZK)
    add_translation(CANNOT_DECIDE_EQUALITY_OF_POINTS_A_B, DE, 'Kann die Gleichheit der Punkte %0 und %1 nicht entscheiden.', ZK)
    add_translation(CANNOT_DECIDE_EQUALITY_OF_POINTS_A_B, ES, 'No se puede decidir la igualdad de los puntos %0 y %1.', ZK)
    add_translation(CANNOT_DECIDE_EQUALITY_OF_POINTS_A_B, HU, 'Nem tudom eldönteni, hogy a(z) %0 és %1 pontok megegyeznek-e.', ZK)

    add_command(COMPARE, 'Compare')
    add_command(COMPARE_SYNTAX, 'Compare.Syntax')
    add_menu(COMPARE_A_AND_B, 'CompareAandB')
    add_translation(COMPARE, EN, 'Compare', ZK)
    add_translation(COMPARE, DE, 'Vergleiche', ZK)
    add_translation(COMPARE, ES, 'Compara', ZK)
    add_translation(COMPARE, HU, 'Összehasonlít', ZK)
    add_translation(COMPARE_SYNTAX, EN, '[ <Expression>, <Expression> ]', ZK)
    add_translation(COMPARE_SYNTAX, ES, '[ <Expresión>, <Expresión> ]', ZK)
    add_translation(COMPARE_SYNTAX, DE, '[ <Ausdruck>, <Ausdruck> ]', ZK)
    add_translation(COMPARE_SYNTAX, HU, '[ <Kifejezés>, <Kifejezés> ]', ZK)
    add_translation(COMPARE_A_AND_B, EN, 'Compare %0 and %1.', ZK)

    add_command(INCIRCLECENTER, 'IncircleCenter')
    add_command(INCIRCLECENTER_SYNTAX, 'IncircleCenter.Syntax')
    add_menu(INCIRCLECENTER_TOOL, 'IncircleCenter')
    add_menu(INCIRCLECENTER_TOOL_HELP, 'IncircleCenter.Help')
    add_translation(INCIRCLECENTER, EN, 'IncircleCenter', ZK)
    add_translation(INCIRCLECENTER, HU, 'BeírtKörKözéppontja', ZK)
    add_translation(INCIRCLECENTER, DE, 'Inkreismittelpunkt', ZK)
    add_translation(INCIRCLECENTER, ES, 'CentroCircunferenciaInscrita', ZK)
    add_translation(INCIRCLECENTER_SYNTAX, EN, '[ <Point>, <Point>, <Point> ]', ZK)
    add_translation(INCIRCLECENTER_SYNTAX, HU, '[ <Pont>, <Pont>, <Pont> ]', ZK)
    add_translation(INCIRCLECENTER_SYNTAX, DE, '[ <Punkt>, <Punkt>, <Punkt> ]', ZK)
    add_translation(INCIRCLECENTER_SYNTAX, ES, '[ <Punto>, <Punto>, <Punto> ]', ZK)
    add_translation(INCIRCLECENTER_TOOL, ES, 'Centro de la circunferencia inscrita', ZK)
    add_translation(INCIRCLECENTER_TOOL, EN, 'Incircle Center', ZK)
    add_translation(INCIRCLECENTER_TOOL, DE, 'Inkreismittelpunkt', ZK)
    add_translation(INCIRCLECENTER_TOOL, HU, 'Beírt kör középpontja', ZK)
    add_translation(INCIRCLECENTER_TOOL_HELP, EN, 'Select three points', ZK)
    add_translation(INCIRCLECENTER_TOOL_HELP, ES, 'Selecciona tres puntos', ZK)
    add_translation(INCIRCLECENTER_TOOL_HELP, DE, 'Gib drei Punkte an', ZK)
    add_translation(INCIRCLECENTER_TOOL_HELP, HU, 'Három pont kijelölése', ZK)

    add_menu(INCIRCLE_TOOL, 'Incircle')
    add_menu(INCIRCLE_TOOL_HELP, 'Incircle.Help')
    add_translation(INCIRCLE_TOOL, EN, 'Incircle', ZK)
    add_translation(INCIRCLE_TOOL, DE, 'Inkreis', ZK)
    add_translation(INCIRCLE_TOOL, ES, 'Circunferencia inscrita', ZK)
    add_translation(INCIRCLE_TOOL, HU, 'Beírt kör', ZK)
    add_translation(INCIRCLE_TOOL_HELP, HU, 'Három pont kijelölése', ZK)
    add_translation(INCIRCLE_TOOL_HELP, ES, 'Selecciona tres puntos', ZK)
    add_translation(INCIRCLE_TOOL_HELP, DE, 'Gib drei Punkte an', ZK)
    add_translation(INCIRCLE_TOOL_HELP, EN, 'Select three points', ZK)

    add_menu(LOCUSEQUATION_TOOL, 'LocusEquation.Tool')
    add_menu(LOCUSEQUATION_TOOL_HELP, 'LocusEquation.Help')
    add_translation(LOCUSEQUATION_TOOL, ES, 'Ecuación Lugar Geométrico', ZK)
    add_translation(LOCUSEQUATION_TOOL, DE, 'Ortsliniengleichung', ZK)
    add_translation(LOCUSEQUATION_TOOL, EN, 'Locus Equation', ZK)
    add_translation(LOCUSEQUATION_TOOL, HU, 'Mértani hely egyenlete', ZK)
    add_translation(LOCUSEQUATION_TOOL_HELP, EN, 'Select locus point, then point on object', ZK)
    add_translation(LOCUSEQUATION_TOOL_HELP, DE, 'Wähle einen Punkt zum Erzeugen der Ortslinie, dann einen Punkt auf einem Objekt', ZK)
    add_translation(LOCUSEQUATION_TOOL_HELP, ES, 'Punto del lugar geométrico; luego, punto en objeto', ZK)
    add_translation(LOCUSEQUATION_TOOL_HELP, HU, 'Mértani hely pontja, majd pont az objektumon', ZK)

    add_menu(ENVELOPE_TOOL, 'Envelope.Tool')
    add_menu(ENVELOPE_TOOL_HELP, 'Envelope.Help')
    add_translation(ENVELOPE_TOOL, EN, 'Envelope', ZK)
    add_translation(ENVELOPE_TOOL, DE, 'Einhüllende', ZK)
    add_translation(ENVELOPE_TOOL, ES, 'Envolvente', ZK)
    add_translation(ENVELOPE_TOOL, HU, 'Burkoló', ZK)
    add_translation(ENVELOPE_TOOL_HELP, EN, 'Select path, then point on object', ZK)
    add_translation(ENVELOPE_TOOL_HELP, DE, 'Gib eine Kurve an, dann einen Punkt auf einem Pfad', ZK)
    add_translation(ENVELOPE_TOOL_HELP, ES, 'Trayecto del envolvente; luego, punto en objeto', ZK)
    add_translation(ENVELOPE_TOOL_HELP, HU, 'Görbe, amelynek burkolóját keressük, majd egy alakzaton mozgó pont', ZK)

    add_menu(PROVE_THAT_A, 'ProveThatA')
    add_menu(LET_A_BE_ARBITRARY_POINTS, 'LetABeArbitraryPoints')
    add_menu(LET_A_BE_THE_B, 'LetABeTheB')
    add_menu(LET_A_BE_A_B, 'LetABeAB')
    add_menu(LET_A_BE_THE_REGULAR_POLYGON_BCD, 'LetABeTheRegularPolygonBCD')
    add_menu(LET_A_BE_THE_REGULAR_BGON_VERTICES_C, 'LetABeTheRegularBGonVerticesC')
    add_menu(DENOTE_THE_EXPRESSION_A_BY_B, 'DenoteTheExpressionAByB')
    add_translation(PROVE_THAT_A, EN, 'Prove that %0.', ZK)
    add_translation(LET_A_BE_ARBITRARY_POINTS, EN, 'Let %0 be arbitrary points.', ZK)
    add_translation(LET_A_BE_THE_B, EN, 'Let %0 be the %1.', ZK)
    add_translation(LET_A_BE_A_B, EN, 'Let %0 be a %1.', ZK)
    add_translation(LET_A_BE_THE_REGULAR_POLYGON_BCD, EN, 'Let %0 be the regular %3-gon over the segment %1, %2.', ZK)
    add_translation(LET_A_BE_THE_REGULAR_BGON_VERTICES_C, EN, 'Let %0 be the regular %1-gon with vertices %2.', ZK)
    add_translation(DENOTE_THE_EXPRESSION_A_BY_B, EN, 'Denote the expression %0 by %1.', ZK)

    add_command(REALQUANTIFIERELIMINATION, 'RealQuantifierElimination')
    add_command(REALQUANTIFIERELIMINATION_SYNTAX, 'RealQuantifierElimination.Syntax')
    add_translation(REALQUANTIFIERELIMINATION, EN, 'RealQuantifierElimination', ZK)
    add_translation(REALQUANTIFIERELIMINATION, DE, 'ReelleQuantorenelimination', ZK)
    add_translation(REALQUANTIFIERELIMINATION_SYNTAX, EN, '[ <Expression> ]', ZK)
    add_translation(REALQUANTIFIERELIMINATION_SYNTAX, DE, '[ <Ausdruck> ]', ZK)
