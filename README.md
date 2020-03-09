# GeoGebra Discovery

This project is dedicated to maintain a [temporary fork](https://github.com/kovzol/geogebra)
of [GeoGebra](https://github.com/geogebra/geogebra) that extends the official version with
some experimental features like

* updates and bugfixes to the Automated Reasoning Tools (ART) (see some YouTube videos
on the [Discover](https://www.youtube.com/playlist?list=PLQ71P_dimzuUGfzDk9jtC5Uy2I3dOn7QQ)
and the [Compare](https://www.youtube.com/playlist?list=PLQ71P_dimzuUNNOSoZkIhaqU3yCa1Y3Ob) commands
for some introductory ideas),
* other bugfixes that are relevant to Classic 5 and Classic 6.

Most of the features are considered unstable. It is planned that after making them stable,
they will be added to the official version of GeoGebra as well.

The files in this project are used to compile and deploy GeoGebra Discovery.

## Releases

End users may want to download one of the most recent [releases](https://github.com/kovzol/geogebra/releases). Then:

* First you need to [install Java RE](https://www.java.com/en/download/)
(unless it is already installed on your computer).
* To run GeoGebra Discovery, you need to extract the downloaded archive and run the file **GeoGebra-Discovery.bat**
(or **GeoGebra-Discovery** on non-Windows systems).

### Web version

The web version is available online at [autogeo.online](http://autgeo.online) and usually updated on every new release.
This version can be downloaded and run offline as well at [autgeo.online/off](http://autgeo.online/off).

## Prerequisites, compilation, running and deployment

You may decide to compile GeoGebra Discovery on your own.

If you do so, you will need a typical Linux system to make the software work.
In particular, the provided scripts were tested on Ubuntu 18.04 and 19.10 (64-bit), and
partially on [Raspbian](http://downloads.raspberrypi.org/raspbian/) Buster (both Raspberry Pi 3 and 4 should work,
however you need at least 2 GB of memory for compilation).

The following tools are available:

### Classic 5

* Type `./get-build-tools` to download some prerequisites including an appropriate
Java Development Kit on Ubuntu 18.04. On Raspberry Pi, a recent version of Giac
will be downloaded and the default Java 11 (OpenJDK) will be used.
* Run `./build5` to build GeoGebra Discovery. This will also build
[RealGeom](https://github.com/kovzol/realgeom).
* Enter `./run5` to start the software. On a Raspberry Pi (or, if Mathematica is available locally) this will also use a local
RealGeom service.
* The command `./deploy5` will create a .zip file that contains all necessary components
to run the program. In case you need a .zip file for Windows users, enter `./deploy5 win`.

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
Carlos Ueno, Manuel Ladra, Pilar Paez and Jonathan Yu for their support.

## Bugs

The database of issues is available at [YouTrack](https://geogebra-prover.myjetbrains.com/youtrack/issues).

## Benchmarks
The [benchmarking system](https://prover-test.geogebra.org/) collects results and speed related information on a daily basis for the [Prove](https://wiki.geogebra.org/en/Prove_Command), [ProveDetails](https://wiki.geogebra.org/en/Prove_Command), [LocusEquation](https://wiki.geogebra.org/en/LocusEquation_Command) and [Envelope](https://wiki.geogebra.org/en/Envelope_Command) commands.

### Latest outputs
* [Prove test](https://prover-test.geogebra.org/job/GeoGebra_Discovery-provertest/lastSuccessfulBuild/artifact/fork/geogebra/test/scripts/benchmark/prover/html/all.html)
* [LocusEquation/Envelope test](https://prover-test.geogebra.org/job/GeoGebra_Discovery-art-plottertest/lastSuccessfulBuild/artifact/fork/geogebra/test/scripts/benchmark/art-plotter/html/all.html)

### All outputs
* [Prove test](https://prover-test.geogebra.org/job/GeoGebra_Discovery-provertest/)
* [LocusEquation/Envelope test](https://prover-test.geogebra.org/job/GeoGebra_Discovery-art-plottertest/)
