# GeoGebra Discovery

This project is dedicated to maintain a [temporary fork](https://github.com/kovzol/geogebra)
of [GeoGebra](https://github.com/geogebra/geogebra) that extends the official version with
some experimental features like

* updates and bugfixes to the Automated Reasoning Tools (ART),
* other bugfixes that are relevant to Classic 5 and Classic 6.

The files in this project are used to compile and deploy GeoGebra Discovery.

## Prerequisites, compilation, running and deployment

You will need a typical Linux system to make the software work.
In particular, the scripts were tested on an Ubuntu 18.04 (64-bit), and
partially on [Raspbian](http://downloads.raspberrypi.org/raspbian/) Buster (both Raspberry Pi 3 and 4 should work,
however you need at least 2 GB of memory for compilation).

The following tools are available:

### Classic 5

* Type `./get-build-tools` to download some prerequisites including an appropriate
Java Development Kit on Ubuntu 18.04. On Raspberry Pi, a recent version of Giac
will be downloaded and the default Java 11 (OpenJDK) will be used.
* Run `./build5` to build GeoGebra Discovery. On a Raspberry Pi this will also build
[RealGeom](https://github.com/kovzol/realgeom).
* Enter `./run5` to start the software. On a Raspberry Pi this will also use a local
RealGeom service.
* The command `./deploy5` will create a .zip file that contains all necessary components
to run the program.

### Classic 6

* Type `./get-build-tools` to download the prerequisites.
* Run `./build6` to build GeoGebra Discovery. (Due to lack of memory this will not work
on Raspberry Pi.)
* Enter `./run6` to start the software.
* The command `./deploy6` creates a .zip file that contains all necessary components
to run the program.

## Authors

GeoGebra is written by its [authors](https://www.geogebra.org/team).

Maintainer of GeoGebra Discovery is Zoltán Kovács <zoltan@geogebra.org>.
