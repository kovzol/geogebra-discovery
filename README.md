# GeoGebra Discovery

This project is dedicated to maintain a [temporary fork](https://github.com/kovzol/geogebra)
of [GeoGebra](https://github.com/geogebra/geogebra) that extends the official version with
some experimental features like

* updates and bugfixes to the Automated Reasoning Tools (ART) (see some YouTube videos
on the [Discover](https://www.youtube.com/playlist?list=PLQ71P_dimzuUGfzDk9jtC5Uy2I3dOn7QQ)
and the [Compare](https://www.youtube.com/playlist?list=PLQ71P_dimzuUNNOSoZkIhaqU3yCa1Y3Ob) commands
for some introductory ideas),
* other bugfixes that are relevant to Classic 5 and Classic 6.

Most of the [features](#feature-matrix) are considered unstable. It is planned that after making them stable,
they will be added to the official version of GeoGebra as well.

The files in this project are used to compile and deploy GeoGebra Discovery.

## Releases

### Desktop version (Classic 5)

End users may want to download one of the most recent [releases](https://github.com/kovzol/geogebra/releases). Then:

* To run GeoGebra Discovery, you need to extract the downloaded archive and run the file **GeoGebra-Discovery.bat**
(or **GeoGebra-Discovery** on non-Windows systems). A short video [tutorial](https://www.youtube.com/watch?v=S1upzsdcW10) is also available.
* In case the program does not start, you need to [install Java RE](https://www.java.com/en/download/).

### Web version (Classic 6)

The web version is available online at [autogeo.online](https://autgeo.online) and usually updated on every new release.
This version can be downloaded and run offline as well at [autgeo.online/off](https://autgeo.online/off).

Please note that the web version cannot solve any problems in real geometry at the moment.
For this purpose you need to download the desktop version.

## Prerequisites, compilation, running and deployment

![build](https://github.com/kovzol/geogebra/workflows/build/badge.svg)

You may decide to compile GeoGebra Discovery on your own.

If you do so, you will need a typical Linux system to make the software work.
In particular, the provided scripts were tested on Ubuntu 18.04 and 19.10 (64-bit), and
partially on [Raspbian](http://downloads.raspberrypi.org/raspbian/) Buster (both Raspberry Pi 3 and 4 should work,
however you need at least 2 GB of memory for compilation). The latest version also works on Mac OS 10.15 Catalina.

The following tools are available:

### Classic 5

* Type `./get-build-tools` to download some prerequisites including an appropriate
Java Development Kit on Ubuntu 18.04 or on Mac. On Raspberry Pi and on newer Ubuntu systems the default Java 11 (OpenJDK) will be used.
* Run `./build5` to build GeoGebra Discovery. This will also build
[RealGeom](https://github.com/kovzol/realgeom).
* Enter `./run5` to start the software. On a Raspberry Pi (or, if Mathematica is available locally) this will also use a local
RealGeom service.
* The command `./deploy5` will create a .zip file that contains all necessary components
to run the program. In case you need a .zip file for Windows users, enter `./deploy5 win`.
Mac users should use the command line `./deploy5 -j lin-force`.
This tool comes with a built-in help that can be invoked by the `-h` option.

### Classic 6

* Type `./get-build-tools` to download the prerequisites.
* Run `./build6` to build GeoGebra Discovery. (Due to lack of memory this will not work
on Raspberry Pi.)
* Enter `./run6` to start the software.
* The command `./deploy6` creates a .zip file that contains all necessary components
to run the program.

## Authors

GeoGebra is written by its [authors](https://www.geogebra.org/team).

* Maintainer of GeoGebra Discovery is Zoltán Kovács <zoltan@geogebra.org>.
* Thanks to Tomás Recio, M. Pilar Vélez, Noah Dana-Picard, Róbert Vajda, Antonio Montes, Francisco Botana, Pavel Pech,
Carlos Ueno, Manuel Ladra, Pilar Paez, Celina Abar and Jonathan Yu for their support.

## Mailing list

A public list is available at [Google Groups](https://groups.google.com/forum/#!forum/geogebra-discovery).

## Feature matrix

This table is ordered by maturity.

| Feature | GeoGebra 	  | GeoGebra Discovery    | Next step  |
|:-------	|:---------:	|:-------------------:	|:---------: |
| Symbolic angle bisectors (prover) | slow | [fast](https://matek.hu/zoltan/blog-20200929.php) | ![approve](images/green.png) GeoGebra Team: approve |
| Algebraic curves as inputs in locus computations | no | [yes](https://matek.hu/zoltan/blog-20201031.php) | ![approve](images/green.png) GeoGebra Team: approve |
| Incircle | numerical command only	| [prover support](https://matek.hu/zoltan/blog-20200929.php) | ![approve](images/green.png) GeoGebra Team: approve |
| IncircleCenter command | no	| [yes (with prover support)](https://matek.hu/zoltan/blog-20200929.php) | ![approve](images/green.png) GeoGebra Team: approve |
| Compare command | no | yes | ![approve](images/orange.png) GeoGebra Team: approve/update |
| Incircle tool | no	| [yes](https://matek.hu/zoltan/blog-20200929.php) | ![approve](images/orange.png) GeoGebra Team: approve/update |
| IncircleCenter tool | no	| [yes](https://matek.hu/zoltan/blog-20200929.php) | ![approve](images/orange.png) GeoGebra Team: approve/update (discuss [Center(Incircle)](https://geogebra-prover.myjetbrains.com/youtrack/issue/TP-53) first) |
| LocusEquation	tool | no | yes	| ![approve](images/orange.png) GeoGebra Team: approve/update |
| Envelope tool | no	| [yes](https://matek.hu/zoltan/blog-20201111.php) | ![approve](images/orange.png) GeoGebra Team: approve/update |
| Raspberry Pi 3D View | no | yes | ![approve](images/orange.png) GeoGebra Team: approve/update |
| Discover tool/command	| no | beta	| ![approve](images/red.png) [Progress bar](https://geogebra-prover.myjetbrains.com/youtrack/issue/TP-53) |
| ApplyMap command | no | prototype | ![approve](images/red.png) Explanation needed |

## Bugs

The database of issues is available at [YouTrack](https://geogebra-prover.myjetbrains.com/youtrack/issues).

## Benchmarks
The [benchmarking system](https://prover-test.geogebra.org/) collects results and speed related information on a daily basis for the [Prove](https://wiki.geogebra.org/en/Prove_Command), [ProveDetails](https://wiki.geogebra.org/en/Prove_Command), [LocusEquation](https://wiki.geogebra.org/en/LocusEquation_Command), [Envelope](https://wiki.geogebra.org/en/Envelope_Command) and Compare commands.

### Latest outputs
* [Prove/ProveDetails test](https://prover-test.geogebra.org/job/GeoGebra_Discovery-provertest/lastSuccessfulBuild/artifact/fork/geogebra/test/scripts/benchmark/prover/html/all.html)
* [LocusEquation/Envelope test](https://prover-test.geogebra.org/job/GeoGebra_Discovery-art-plottertest/lastSuccessfulBuild/artifact/fork/geogebra/test/scripts/benchmark/art-plotter/html/all.html)
* [Compare test](https://prover-test.geogebra.org/job/GeoGebra_Discovery-comparetest/lastSuccessfulBuild/artifact/fork/geogebra/test/scripts/benchmark/compare/html/all.html)

### All outputs
* [Prove/ProveDetails test](https://prover-test.geogebra.org/job/GeoGebra_Discovery-provertest/)
* [LocusEquation/Envelope test](https://prover-test.geogebra.org/job/GeoGebra_Discovery-art-plottertest/)
* [Compare test](https://prover-test.geogebra.org/job/GeoGebra_Discovery-comparetest/)

## References

### Discover command

* [F. Botana, Z. Kovács, T. Recio: Towards an Automated Geometer (AISC 2018: Artificial Intelligence and Symbolic Computation, p. 215-220)](https://link.springer.com/chapter/10.1007/978-3-319-99957-9_15)
* [Z. Kovács, J. H. Yu: Towards Automated Discovery of Geometrical Theorems in GeoGebra](https://arxiv.org/abs/2007.12447)

### Relation command
* [Z. Kovács: The Relation Tool in GeoGebra 5 (ADG 2014: Automated Deduction in Geometry, p. 53-71)](https://link.springer.com/chapter/10.1007/978-3-319-21362-0_4)

### Prove/ProveDetails commands

* [F. Botana, M. Hohenwarter, P. Janičić, Z. Kovács, I. Petrović, T. Recio, S. Weitzhofer: Automated Theorem Proving in GeoGebra: Current Achievements (Journal of Automated Reasoning 55, p. 39-59, 2015)](https://link.springer.com/article/10.1007/s10817-015-9326-4)

### Compare command

* [C. Abar, Z. Kovács, T. Recio, R. Vajda: Conectando Mathematica e GeoGebra para explorar construções geométricas planas, 2019](https://www.researchgate.net/publication/337499551_Conectando_Mathematica_e_GeoGebra_para_explorar_construcoes_geometricas_planas)
* [R. Vajda, Z. Kovács: GeoGebra and the realgeom Reasoning Tool, 2020](https://www.researchgate.net/publication/345246253_GeoGebra_and_the_realgeom_Reasoning_Tool)
