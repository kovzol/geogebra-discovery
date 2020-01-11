# GeoGebra Discovery

This project is dedicated to maintain a [temporary fork](https://github.com/kovzol/geogebra)
of [GeoGebra](https://github.com/geogebra/geogebra) that extends the official version with
some experimental features like

* updates and bugfixes to the Automated Reasoning Tools (ART),
* other bugfixes that are relevant to Classic 5 and Classic 6.

The files in this project are used to compile and deploy GeoGebra Discovery.

## Prerequisites, compilation, running and deployment

You will need a typical Linux system to make the software work.
In particular, the scripts were tested on an Ubuntu 18.04, and
partially on Raspbian Buster.

The following tools are available:

### Classic 5

* Type `./get-build-tools` to download some prerequisites including an appropriate
Java Development Kit.
* Run `./build5` to build GeoGebra Discovery.
* Enter `./run5` to start the software.

### Classic 6

* Type `./get-build-tools` to download the prerequisites.
* Run `./build6` to build GeoGebra Discovery.
* Enter `./run6` to start the software.

## Authors

GeoGebra is written by its [authors](https://www.geogebra.org/team).

Maintainer of GeoGebra Discovery is Zoltan Kovacs <zoltan@geogebra.org>.
