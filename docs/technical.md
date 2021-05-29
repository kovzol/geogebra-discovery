# Technical documentation

The purpose of this document is to highlight those changes in GeoGebra
Discovery that were needed to implement some missing features that
are not present in the official version of GeoGebra. These pieces
of information can be important on merging the two codebases.

## JOGL 2.4

Official GeoGebra uses JOGL 2.2. While it is not necessary for its
internals, GeoGebra Discovery already uses JOGL 2.4. This means that
instead of `javax.media` the package `com.jogamp` must be used in the
Java sources. A transition should be not more complicated than doing some
minor refactoring. Also, `$joglversion` needs to be updated in the Gradle
build machinery.

## ARM support (Raspberry Pi)

Each time GeoGebra Discovery requires an updated version of Giac,
a manual compilation of Giac is needed for the ARM architecture.
For some reason, Gradle cannot handle different versions for
native packages, so we need the same version of Giac uniformly.

## Localization of new features

GeoGebra's official translation system is a closed source application
that maintains a database of translation strings. Here we store a copy of
a new script, [patch.py](patch.py), to add extra entries to the database.

## Giac's thread on Linux

In the official version, for former stability issues, Giac calls are not
running in a thread under Linux. This has been changed in GeoGebra
Discovery and seems to work safely. This is handled in `CasGiacD`.

## Desktop 5 update on Windows

GeoGebra Discovery has no automatic update. This feature of official
GeoGebra has been disabled in `GeoGebraFrame`.

## Version info in Desktop 5

`GeoGebraMenuBar.showAboutDialog()` contains the code the show
the current version of GeoGebra Discovery.

`GeoGebraConstants` contains the recent version info.

## Splash screen in the web version

Tomás Recio did an enormous work on popularizing GeoGebra Discovery.
So the splash screen includes his photo and some acknowledgments
in the web version.

Here there are some technical extensions to fix the amount of time to
show the splash screen. This does not work well in official GeoGebra.

See `AppResources`, `ImageResource geogebraLogo()`.
Also, `SplashDialog.SplashDialog()` and `ggbSplash.html`.

## Prover

### Trichotomy of proof results

`GeoBoolean.toString()` needed to be hotfixed to ensure showing `undefined`
in the Algebra View.

### Decreased verbosity of the threaded prover

Too frequent report in `ProverD` is annoying, so it is a bit muted in
GeoGebra Discovery.

### RealGeom WebService

The realgeom subsystem is supported via the classes `RealGeomWebService`
and `RealGeomWSSettings`. It is more or less implemented in the same
way as the Singular Web Service, already available in official GeoGebra
for a long time.

The RealGeom WebService is initialized in `AppD`. Currently, a locally
installed version of [realgeom](https://github.com/kovzol/realgeom) is
assumed by the startup scripts of GeoGebra Discovery. If it is not
present, a remote installation can also be used. By default, GeoGebra
Discovery assumes the presence of a remote installation (and its hostname
is hardcoded), but this may be removed in a future version.

For the long term, we would like to integrate RealGeom inside GeoGebra
and outsource computations to a DLL version of Tarski/QEPCAD (or
SMT-RAT).

### Better handling of `:` in the command line options

The character `:` is used to separate an option name and its value.
Sometimes, however, this character is also used in values, mostly
in HTTP requests. To solve this issues, one needs to write `\:`
in such cases, in the value part. See `AppD` and search for `_COLON_`.

### CAS starts automatically

GeoGebra Discovery requires to have access to the CAS immediately.
This is currently ensured by forcing an initial CAS call
in `AppW.initCoreObjects()`.

### Frame title

`updateFrameTitle()` in `GuiManagerW` and `GuiManagerD` now has a
parameter that can be shown as message in the title of the application
window. This is used in the Discover command to give some feedback on the
state of procession.

### Editable rows in a relation popup, modal window

`RelationPaneW` and `RelationPaneD` now have the `changeRowLeftColumn()`
method to support changing existing data in a row.

The Relation window is now modal. On some systems, including macOS,
the Relation window remained hidden unless it is not set modal.
See `RelationPaneD` for details.

### Discovery pool

Each `Construction` uses its own discovery `Pool`. It is a database of
geometric properties being found and proven by the Discover command.
In some sense, this is a simple cache, but its update is non-trivial.

Each time a new file or window is opened, or an undo/redo operation
is issued, the discovery pool must be initialized.

On point removal the discovery pool must be updated accordingly.

The following changes were required:

1. In `GeoPoint.doRemove()`, before the last line `super.doRemove()`
`cons.getDiscoveryPool().removePoint((GeoPoint) this)` must be called.
2. In `Construction` 3 new definitions were reqiured:
`private Pool discoveryPool = new Pool();`,
`public Pool getDiscoveryPool() { return discoveryPool; }` and
`public void initDiscoveryPool() { discoveryPool = new Pool(); }`.
3. In `Construction`, the last line in the constructor a
`initDiscoveryPool()` is required. Also for `undo()` and `redo()`.
4. In `AppD.setCurrentFile(File file)` the first command should be
`getKernel().getConstruction().initDiscoveryPool()`.
Also in `AppW.setCurrentFile(GgbFile file)`.
5. In `GeoElement.isRedefineable()` there is some more sophisticated
code (ca. 10 lines): for the moment no line or circle can be redefined
if there is an entry of it in the pool.

### TreeMap instead of HashMap

To ensure deterministic computations, ordering of variables should be
deterministic. Therefore TreeMap should be used instead of HashMap, and
TreeSet instead of HashSet. In some occurrences there are already changes
according to this, but not everywhere (yet).

The same has been done for the `NDGCondition` class in the prover.
This ensures alphabetical ordering of the conditions, it is useful
on deterministic lists.

### [Geometric discovery](https://geogebra-prover.myjetbrains.com/youtrack/issue/TP-14) (proposed by Tim Brzezinski)

This feature is present for a long time, but enabled only
in GeoGebra Discovery.

### New tools: Incircle, IncircleCenter, Envelope, LocusEquation, Discover

These are added in GeoGebra Discovery only. See, among others, `ToolBar`
(to set the default toolbar), `GGWToolBar`, `ToolbarSvgResources` and
`ToolbarResources`. 

### New commands: Compare, IncircleCenter, Discover

These are added in GeoGebra Discovery only.

### Caption algebra mode

`GeoElement.setCaptionBotanaVars()` and `.addCaptionBotanaPolynomial` had to
be updated and the geo required an `update()`.
