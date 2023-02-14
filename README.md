GeoGebra Discovery is an experimental version of [GeoGebra](https://www.geogebra.org). It contains some
bleeding edge features of GeoGebra that are under heavy development and therefore not intended for every day use yet,
so they are not included in the official GeoGebra version.
Also, in some cases, there is no consensus on whether to include certain
elements in GeoGebra or to leave them out (for example, because they are
too specific for a particular audience).

We maintain a [feature list](#feature-matrix). Some features are considered unstable, but many of them are mature
and ready to try by anyone, and technically close to be able to being integrated into GeoGebra shortly.
It is planned that each feature, after made stable, will be added to the official version of GeoGebra as well,
but the GeoGebra Team may decide to leave some features out for technical, practical or didactical reasons.
Anyway, we are doing our best and are open for discussion.

Technically speaking, GeoGebra Discovery is based on the freely available [GitHub sources of GeoGebra](https://github.com/geogebra/geogebra) which is maintained by the [GeoGebra Team](https://www.geogebra.org/team).
We maintain a [fork](https://github.com/kovzol/geogebra) for revision control of the extensions. In addition, this
web page has the following purposes:
* For end users, we point to the software packages that make possible to install and run GeoGebra Discovery on your computer.
* For end users, we explain the additions of GeoGebra Discovery compared to the official version of GeoGebra by short descriptions.
* For researchers, we provide a list of web references (research papers, links, benchmarks) for the additions.
* For programmers, we explain how to try the latest unstable version of GeoGebra Discovery. For this purpose we provide some scripts and programmatic tools.

## Download a stable release

### Desktop version (Classic 5)

End users may want to [download one of the most recent releases](https://github.com/kovzol/geogebra/releases). Then:

* To run GeoGebra Discovery, you need to extract the downloaded archive and run the file **GeoGebra-Discovery.bat**
(or **GeoGebra-Discovery** on non-Windows systems). A short video [tutorial](https://www.youtube.com/watch?v=S1upzsdcW10) is also available.
* In case the program does not start, you need to [install Java RE](https://www.java.com/en/download/).

For Linux users, the simplest way is to get GeoGebra Discovery from the Snap Store:

[![Get it from the Snap Store](https://snapcraft.io/static/images/badges/en/snap-store-black.svg)](https://snapcraft.io/geogebra-discovery)

### Web version (Classic 6)

The web version is available online at [autogeo.online](https://autgeo.online) and usually updated on every new release.
This version can be downloaded and run offline as well at [autgeo.online/off](https://autgeo.online/off).

## Try the latest unstable version: Prerequisites, compilation, running and deployment

This section can be technically challenging. If you are not familiar with program development, it is safer to use a stable release (see above).

![build](https://github.com/kovzol/geogebra-discovery/workflows/build/badge.svg)

You may decide to compile GeoGebra Discovery on your own.

If you do so, you will need a typical Linux, Mac or Windows system to make the software work.
The provided scripts were tested on Ubuntu Linux 20.04 and above (64-bit),
and partially on [Raspbian](http://downloads.raspberrypi.org/raspbian/) Buster (both Raspberry Pi 3 and 4 should work,
however you need at least 2 GB of memory for compilation). 
The latest versions also work on Mac OS 11 Big Sur, see the required steps below.
Finally, you can use Windows 10 as well to compile and run GeoGebra Discovery.

### Classic 5

The current version automatically downloads a release version of [Tarski](https://www.usna.edu/Users/cs/wcbrown/tarski/index.html) 1.30.
In addition, the [RealGeom](https://github.com/kovzol/realgeom) system will be built, but not packaged or used, only when it is requested by the user
(or, if the platform is the Raspberry Pi system). See below the detailed instructions.

#### Steps to build GeoGebra Discovery on Linux

These steps were tested on Ubuntu, and they may not work on other Linux systems.

* Open a terminal and type `./get-build-tools` to download some prerequisites including an appropriate
Java Development Kit on Ubuntu Linux. On Raspberry Pi and on newer Ubuntu systems the default Java 11 (OpenJDK) may also be used,
so you can skip this step.
* Run `./build5` to build the complete GeoGebra Discovery system.
* Enter `./run5` to start the software.
* If you want to make a copy of the program for redistribution, the command `./deploy5` will create a .zip file that contains all necessary components
to run the program.
(The deployment tool comes with a built-in help that can be invoked by the `-h` option.)

#### Steps to build GeoGebra Discovery on macOS

* Start Terminal: Press Cmd+Space to open spotlight search, and type terminal and hit return.
* Type `git clone https://github.com/kovzol/geogebra-discovery` to download the source code.
* Type `cd geogebra-discovery` to change the working directory.
* Type `./get-build-tools` to get Java.
* Type `./build5` to build GeoGebra Discovery.
* Type `./run5` to test if GeoGebra Discovery runs properly.
* If you want to make a copy of the program for redistribution, type `./deploy5 -j` to create a **.zip** bundle that contains all necessary files for GeoGebra Discovery.
The bundle will be put in the relative folder **dist/**. (In case your working directory is **/tmp/**, you may want
to copy the **.zip** bundle to another folder, say, your home folder, to avoid deletion of all your created files
on an accidental reboot.)

#### Steps to build GeoGebra Discovery on Windows 10

On Windows we support both 64 and 32-bit builds. However, 32-bit builds are considered experimental.
* Set **Developer Mode** in Windows.
* Open a Powershell window as administrator. [Install Chocolatey](https://chocolatey.org/install).
  Install MSYS2 by typing `choco install msys2` in the Powershell prompt.
* If you plan to compile GeoGebra Discovery for 64-bit systems,
  start MSYS2/CLANG64 by starting the executable `clang64` in `C:\tools\msys64\` (we assume this is the correct installation folder).
  Alternatively, you may use MSYS2/CLANG32 if you want to create a 32-bit package.
* Install [Microsoft's Java 11](https://www.microsoft.com/openjdk) if you want a 64-bit build. It is safe to use the Windows x64 .msi version.
  Alternatively, you can download a different Java JDK for a 32-bit build. Oracle's Java 1.8 has been successfully tested.
* Install [Git for Windows](https://gitforwindows.org) (version 2.32.0(2) should work).
  Use the default settings during the installation, but enable symbolic links (this option is disabled by default).
* Open **Git Bash** and type `git clone https://github.com/kovzol/geogebra-discovery`.
* Go back to the MSYS2/CLANG64 window and change your working directory to see the folder from the previous step.
  This can be set with a command like `cd /c/Users/<username>/geogebra-discovery` where `<username>` stands for you username on Windows.
* Type `./build5` to build the program.
* Type `./run5` to test if GeoGebra Discovery runs properly.
* In case you want to create a redistribution package, you need to install two more tools in the MSYS2 subsystem.
  Type `pacman -S rsync zip` first. Then run `./deploy5` to create a **.zip** bundle for redistribution.

#### Force running realgeom

This feature is disabled by default on all system, except on a Raspberry Pi.
You may want to use realgeom if you intend to outsource the real geometry computations to Mathematica.
These are the steps you need to achieve this:

* Build the program (see above).
* Run `helper/realgeom` to start the realgeom server. It will run in a separate terminal.
* Start GeoGebra Discovery by using the command line `./run5 --realgeomws=enable:true,remoteurl:http\://localhost\:8765,cas:mathematica,timeout:10`
for example.

### Classic 6

* Type `./get-build-tools` to download the prerequisites (only on earlier Linux systems and Mac).
* Run `./build6` to build GeoGebra Discovery. (Due to lack of memory this will not work
on Raspberry Pi.)
* Enter `./run6` to start the software. A web browser window should appear and GeoGebra Discovery starts.
* Lastly, the command `./deploy6` creates a .zip file that contains all necessary components
to run the program. This can be necessary if you want to redistribute the software. (This last step will not work on Windows.)

## Authors

GeoGebra is written by its [authors](https://www.geogebra.org/team).

* Maintainer of GeoGebra Discovery is Zoltán Kovács <zoltan@geogebra.org>.
* Thanks to Tomás Recio, M. Pilar Vélez, Noah Dana-Picard, Róbert Vajda, Antonio Montes, Francisco Botana, Pavel Pech,
Carlos Ueno, Manuel Ladra, Pilar Paez, Celina Abar, Jonathan Yu, Keiichi Tsujimoto and Christopher W. Brown for their support.

## Mailing list

A public list is available at [Google Groups](https://groups.google.com/forum/#!forum/geogebra-discovery).

## Feature matrix

### New features

This table is ordered by maturity.

| Feature | GeoGebra 	  | GeoGebra Discovery    | Next step  |
|:-------	|:---------:	|:-------------------:	|:---------: |
| Discover tool/command	| no | [yes](https://matek.hu/zoltan/blog-20201019.php)	| ![approved](images/green.png) Scheduled for merging into GeoGebra |
| Stepwise discovery	| no | [yes](https://matek.hu/zoltan/stepwise/csgg.pdf) | ![approve](images/orange.png) GeoGebra Team: approve/update |
| Compare command | no | [yes](https://matek.hu/zoltan/blog-20210125.php) | ![approve](images/orange.png) GeoGebra Team: approve/update |
| Proving inequalities | no | [yes](https://matek.hu/zoltan/blog-20211028.php) | ![approve](images/orange.png) GeoGebra Team: approve/update |
| RealQuantifierElimination command | no | [yes](https://matek.hu/zoltan/demo-20211118.php) | ![approve](images/orange.png) GeoGebra Team: approve/update |
| Prenex formulas | no | [yes](https://matek.hu/zoltan/blog-20220212.php) | ![approve](images/orange.png) GeoGebra Team: approve/update |
| IncircleCenter command | no	| [yes (with prover support)](https://matek.hu/zoltan/blog-20200929.php) | ![approve](images/orange.png) GeoGebra Team: approve (discuss [Center(Incircle)](https://geogebra-prover.myjetbrains.com/youtrack/issue/TP-53) first) |
| Incircle tool | no	| [yes](https://matek.hu/zoltan/blog-20200929.php) | ![approve](images/orange.png) GeoGebra Team: approve/update |
| IncircleCenter tool | no	| [yes](https://matek.hu/zoltan/blog-20200929.php) | ![approve](images/orange.png) GeoGebra Team: approve/update |
| LocusEquation	tool | no | yes	| ![approve](images/orange.png) GeoGebra Team: approve/update |
| Envelope tool | no	| [yes](https://matek.hu/zoltan/blog-20201111.php) | ![approve](images/orange.png) GeoGebra Team: approve/update |
| Raspberry Pi 3D View | no | yes | ![approve](images/orange.png) GeoGebra Team: approve/update |
| Java OpenGL | 2.2 | 2.4 | ![approve](images/orange.png) GeoGebra Team: approve/update |
| Giac: threads on Linux | no | yes | ![approve](images/orange.png) GeoGebra Team: approve/update |
| Same color for circles with the same radius | no | yes | ![approve](images/orange.png) GeoGebra Team: approve/update |
| Plotting logical connectives of inequalities | partial | [full](https://github.com/kovzol/geogebra/releases/tag/v5.0.641.0-2023Jan27) | ![approve](images/orange.png) GeoGebra Team: approve/update |
| Prenex formulas | no | [prototype](https://matek.hu/zoltan/blog-20220212.php) | ![approve](images/orange.png) GeoGebra Team: approve/update |
| Stepwise discovery	| no | prototype	| ![prototype](images/red.png) Fix some issues |
| Export Construction Protocol as LaTeX | no | prototype	| ![prototype](images/red.png) Implement CAS/Spreadsheet view, add web implementation |
| ApplyMap command | no | [prototype](https://matek.hu/zoltan/blog-20210126.php) | ![prototype](images/red.png) Fix [bugs](https://geogebra-prover.myjetbrains.com/youtrack/issue/TP-60) and make [improvements](https://geogebra-prover.myjetbrains.com/youtrack/issue/TP-58) |
| Plot2D command | no | [prototype](https://github.com/kovzol/geogebra/releases/tag/v5.0.641.0-2023Jan27) | ![prototype](images/red.png) Fix bugs |

### Features that have already been merged

| Feature | GeoGebra version | Date |
|:------- |:--------------------: |:---: |
| [Fast symbolic angle bisectors (prover)](https://matek.hu/zoltan/blog-20200929.php) | 5.0.641.0 | May 2021 |
| [Algebraic curves as inputs in locus computations](https://matek.hu/zoltan/blog-20201031.php) |  5.0.641.0 | May 2021 |
| [Incircle (prover support)](https://matek.hu/zoltan/blog-20200929.php) | 5.0.641.0 | May 2021 |

### [Technical documentation](docs/technical.md)

We maintain a technical documentation to keep some programming related
details up-to-date in order to help a possible merge of the two codebases.

## Bugs

The database of issues is available at [YouTrack](https://geogebra-prover.myjetbrains.com/youtrack/issues).

## Benchmarks
The [benchmarking system](https://prover-test.geogebra.org/) collects results and speed related information on a daily basis for the [Prove](https://wiki.geogebra.org/en/Prove_Command), [ProveDetails](https://wiki.geogebra.org/en/Prove_Command), [LocusEquation](https://wiki.geogebra.org/en/LocusEquation_Command), [Envelope](https://wiki.geogebra.org/en/Envelope_Command) and Compare commands.

### Latest outputs
* [Prove/ProveDetails test](https://prover-test.geogebra.org/job/GeoGebra_Discovery-provertest/lastSuccessfulBuild/artifact/fork/geogebra/test/scripts/benchmark/prover/html/all.html)
* [LocusEquation/Envelope test](https://prover-test.geogebra.org/job/GeoGebra_Discovery-art-plottertest/lastSuccessfulBuild/artifact/fork/geogebra/test/scripts/benchmark/art-plotter/html/all.html)
* [Compare test](https://prover-test.geogebra.org/job/GeoGebra_Discovery-comparetest/lastSuccessfulBuild/artifact/fork/geogebra/test/scripts/benchmark/compare/html/all.html)
* [Discover test](https://prover-test.geogebra.org/job/GeoGebra_Discovery-discovertest/)
* [Prove test (inequalities)](https://prover-test.geogebra.org/job/GeoGebra_Discovery-proverrgtest/lastSuccessfulBuild/artifact/fork/geogebra/test/scripts/benchmark/prover-rg/html/all.html)

### All outputs
* [Prove/ProveDetails test](https://prover-test.geogebra.org/job/GeoGebra_Discovery-provertest/)
* [LocusEquation/Envelope test](https://prover-test.geogebra.org/job/GeoGebra_Discovery-art-plottertest/)
* [Compare test](https://prover-test.geogebra.org/job/GeoGebra_Discovery-comparetest/)
* [Discover test](https://prover-test.geogebra.org/job/GeoGebra_Discovery-discovertest/)
* [Prove test (inequalities)](https://prover-test.geogebra.org/job/GeoGebra_Discovery-proverrgtest/)

## References

* [Z. Kovács, T. Recio, M. P. Vélez: GeoGebra Discovery in Context (ADG 2021: Automated Deduction in Geometry, p. 141-147, 2021)](https://cgi.cse.unsw.edu.au/~eptcs/paper.cgi?ADG2021.16)
* [Z. Kovács, T. Recio, M. P. Vélez: Automated Reasoning Tools in GeoGebra Discovery (ACM Communications in Computer Algebra 55(2), p. 39–43, 2021)](https://dl.acm.org/doi/10.1145/3493492.3493495)

### Discover command

* [F. Botana, Z. Kovács, T. Recio: Towards an Automated Geometer (AISC 2018: Artificial Intelligence and Symbolic Computation, p. 215-220, 2018)](https://link.springer.com/chapter/10.1007/978-3-319-99957-9_15)
* [Z. Kovács, J. H. Yu: Towards Automated Discovery of Geometrical Theorems in GeoGebra, 2020](https://arxiv.org/abs/2007.12447)
* [Z. Kovács, T. Recio: GeoGebra Reasoning Tools for Humans and for Automatons, 2020](https://www.researchgate.net/publication/347256855_GeoGebra_Reasoning_Tools_for_Humans_and_for_Automatons)
* [Z. Kovács: Discovering geometry via the Discover command in GeoGebra Discovery, REMATEC 16(37), p. 14-25, 2021](https://www.researchgate.net/publication/348598407_Discovering_geometry_via_the_Discover_command_in_GeoGebra_Discovery)

### Relation command
* [Z. Kovács: The Relation Tool in GeoGebra 5 (ADG 2014: Automated Deduction in Geometry, p. 53-71, 2015)](https://link.springer.com/chapter/10.1007/978-3-319-21362-0_4)

### Prove/ProveDetails commands

* [F. Botana, M. Hohenwarter, P. Janičić, Z. Kovács, I. Petrović, T. Recio, S. Weitzhofer: Automated Theorem Proving in GeoGebra: Current Achievements (Journal of Automated Reasoning 55, p. 39-59, 2015)](https://link.springer.com/article/10.1007/s10817-015-9326-4)

### Compare command
* [C. Abar, Z. Kovács, T. Recio, R. Vajda: Conectando Mathematica e GeoGebra para explorar construções geométricas planas, 2019](https://www.researchgate.net/publication/337499551_Conectando_Mathematica_e_GeoGebra_para_explorar_construcoes_geometricas_planas)
* [R. Vajda, Z. Kovács: GeoGebra and the realgeom Reasoning Tool, 2020](https://www.researchgate.net/publication/345246253_GeoGebra_and_the_realgeom_Reasoning_Tool)
* [C.W. Brown, Z. Kovács, R. Vajda: Supporting Proving and Discovering Geometric Inequalities in GeoGebra by using Tarski (ADG 2021: Automated Deduction in Geometry, p. 156-166, 2021)](https://cgi.cse.unsw.edu.au/~eptcs/paper.cgi?ADG2021.18)
