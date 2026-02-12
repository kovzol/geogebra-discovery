GeoGebra Discovery is an experimental version of [GeoGebra](https://www.geogebra.org). It contains some bleeding edge features of GeoGebra that are under heavy development and therefore not intended for every day use yet, so they are not included in the official GeoGebra version.
Also, in some cases, there is no consensus on whether to include certain elements in GeoGebra or to leave them out (for example, because they are too specific for a particular audience).

We maintain a [feature list](#feature-matrix). Some features are considered unstable, but many of them are mature and ready to try by anyone, and technically close to be able to being integrated into GeoGebra shortly. It is planned that each feature, after made stable, will be added to the official version of GeoGebra as well, but the GeoGebra Team may decide to leave some features out for technical, practical or didactical reasons. Anyway, we are doing our best and are open for discussion.

Technically speaking, GeoGebra Discovery is based on the freely available [GitHub sources of GeoGebra](https://github.com/geogebra/geogebra) which is maintained by the [GeoGebra Team](https://www.geogebra.org/u/geogebrateam). Here we are working on a [fork](https://github.com/kovzol/geogebra) for revision control of the extensions. In addition, this web page has the following purposes:
* For end users, we point to the software packages that make possible to install and run GeoGebra Discovery on your computer.
* For end users, we explain the additions of GeoGebra Discovery compared to the official version of GeoGebra by short descriptions.
* For researchers, we provide a list of web references (research papers, links, benchmarks) for the additions.
* For programmers, we explain how to try the latest unstable version of GeoGebra Discovery. For this purpose we provide some scripts and programmatic tools.

## Download a stable release

### Desktop version (Discovery 5)

End users may want to [download one of the most recent releases](https://github.com/kovzol/geogebra/releases). Then:

* To run GeoGebra Discovery, you need to extract the downloaded archive and run the file **GeoGebra-Discovery.bat** (or **GeoGebra-Discovery** on non-Windows systems). A short video [tutorial](https://www.youtube.com/watch?v=S1upzsdcW10) is also available.
* In case the program does not start, you need to [install Java RE](https://www.java.com/en/download/).

For Linux users, the simplest way is to get GeoGebra Discovery from Flathub or the Snap Store:

<a href="https://flathub.org/apps/details/io.github.kovzol.geogebra-discovery"><img src="https://flathub.org/api/badge?locale=en" height="56"></a> <a href="https://snapcraft.io/geogebra-discovery"><img src="https://snapcraft.io/static/images/badges/en/snap-store-black.svg" height="60"></a>

### Web version (Discovery 6)

The web version is available online at [autogeo.online](https://autgeo.online) and usually updated on every new release. This version can be downloaded and run offline as well at [autgeo.online/off](https://autgeo.online/off).

## Try the latest unstable version: Prerequisites, compilation, running and deployment

This section can be technically challenging. If you are not familiar with program development, it is safer to use a stable release (see above).

![build](https://github.com/kovzol/geogebra-discovery/workflows/build/badge.svg)

You may decide to compile GeoGebra Discovery on your own.

If you do so, you will need a typical Linux, Mac or Windows system to make the software work. The provided scripts were tested on Ubuntu Linux 20.04 and above (64-bit). The latest versions also work on Mac OS 14 Sonoma, see the required steps below. Finally, you can use Windows 10/11 as well to compile and run GeoGebra Discovery.

### Discovery 5

The current version automatically downloads a release version of [Tarski](https://www.usna.edu/Users/cs/wcbrown/tarski/index.html) 1.37. In addition, the [RealGeom](https://github.com/kovzol/realgeom) system will be built, but not packaged or used, only when it is requested by the user. See below the detailed instructions.

#### Steps to build GeoGebra Discovery on Linux

These steps were tested on Ubuntu, and they may not work on other Linux systems.

* Open a terminal.
* Type `git clone https://github.com/kovzol/geogebra-discovery` to download the source code.
* Type `cd geogebra-discovery` to change the working directory.
* Enter `./get-build-tools` to download some prerequisites including an appropriate Java Development Kit on Ubuntu Linux. On Raspberry Pi and on newer Ubuntu systems the default Java 11 (OpenJDK) may also be used, so you can skip this step.
* Run `./build5` to build the complete GeoGebra Discovery system.
* Enter `./run5` to start the software.
* If you want to make a copy of the program for redistribution, the command `./deploy5` will create a .zip file that contains all necessary components to run the program. (The deployment tool comes with a built-in help that can be invoked by the `-h` option.)

#### Steps to build GeoGebra Discovery on macOS

* Start Terminal: Press Cmd+Space to open spotlight search, and type terminal and hit return.
* Type `git clone https://github.com/kovzol/geogebra-discovery` to download the source code.
* Type `cd geogebra-discovery` to change the working directory.
* Type `./get-build-tools` to get Java.
* Type `./build5` to build GeoGebra Discovery.
* Type `./run5` to test if GeoGebra Discovery runs properly.
* If you want to make a copy of the program for redistribution, type `./deploy5 -j` to create a **.zip** bundle that contains all necessary files for GeoGebra Discovery. The bundle will be put in the relative folder **dist/**. (In case your working directory is **/tmp/**, you may want to copy the **.zip** bundle to another folder, say, your home folder, to avoid deletion of all your created files
on an accidental reboot.)

#### Steps to build GeoGebra Discovery on Windows 10/11

On Windows we support both 64 and 32-bit builds. However, 32-bit builds are considered experimental.
* Set **Developer Mode** in Windows.
* Open a Powershell window as administrator. [Install Chocolatey](https://chocolatey.org/install). Install MSYS2 by typing `choco install msys2` in the Powershell prompt.
* If you plan to compile GeoGebra Discovery for 64-bit systems, start MSYS2/CLANG64 by starting the executable `clang64` in `C:\tools\msys64\` (we assume this is the correct installation folder). Alternatively, you may use MSYS2/CLANG32 if you want to create a 32-bit package.
* Install [Microsoft's Java 11](https://www.microsoft.com/openjdk) if you want a 64-bit build. It is safe to use the Windows x64 .msi version. Alternatively, you can download a different Java JDK for a 32-bit build. Oracle's Java 1.8 has been successfully tested.
* Install [Git for Windows](https://gitforwindows.org) (version 2.32.0(2) should work). Use the default settings during the installation, but enable symbolic links (this option is disabled by default).
* Open **Git Bash** and type `git clone https://github.com/kovzol/geogebra-discovery`.
* Go back to the MSYS2/CLANG64 window and change your working directory to see the folder from the previous step. This can be set with a command like `cd /c/Users/<username>/geogebra-discovery` where `<username>` stands for you username on Windows.
* Type `./build5` to build the program.
* Type `./run5` to test if GeoGebra Discovery runs properly.
* In case you want to create a redistribution package, you need to install two more tools in the MSYS2 subsystem. Type `pacman -S rsync zip` first. Then run `./deploy5` to create a **.zip** bundle for redistribution.

#### Force running realgeom

This feature is disabled by default on all system. You may want to use realgeom if you intend to outsource the real geometry computations to Mathematica. These are the steps you need to achieve this:

* Build the program (see above).
* Run `helper/realgeom` to start the realgeom server. It will run in a separate terminal.
* Start GeoGebra Discovery by using the command line `./run5 --realgeomws=enable:true,remoteurl:http\://localhost\:8765,cas:mathematica,timeout:10` for example.

### Discovery 6

* Type `./get-build-tools` to download the prerequisites (only on earlier Linux systems and Mac).
* Run `./build6` to build GeoGebra Discovery.
* Enter `./run6` to start the software. A web browser window should appear and GeoGebra Discovery starts.
* Lastly, the command `./deploy6` creates a .zip file that contains all necessary components to run the program. This can be necessary if you want to redistribute the software. (This last step will not work on Windows.)

## Authors

GeoGebra is written by its [authors](https://www.geogebra.org/team).

* Maintainer of GeoGebra Discovery is Zoltán Kovács <zoltan@geogebra.org>.
* Thanks to Tomás Recio, M. Pilar Vélez, Noah Dana-Picard, Róbert Vajda, Antonio Montes, Francisco Botana, Pavel Pech, Carlos Ueno, Manuel Ladra, Pilar Paez, Celina Abar, Jonathan H. Yu, Keiichi Tsujimoto and Christopher W. Brown for their support. There are further people who contributed to this work (but not listed above), thanks to everyone!

## License

See [GeoGebra's licensing policy](https://www.geogebra.org/license) for
general information on licensing GeoGebra. Since the developer team of
GeoGebra Discovery does not provide any commercial support, all
extensions (including artwork, translations) to GeoGebra are provided
"as is". In particular, extensions to the source code are licensed to
you under the terms of the GNU General Public License (version 3 or
later) as published by the Free Software Foundation, the current text of
which can be found via this link: https://www.gnu.org/licenses/gpl.html
("GPL"). Attribution (as required by the GPL) should take the form of
(at least) a mention of this project page of GeoGebra Discovery.

## Mailing list

A public list is available at [Google Groups](https://groups.google.com/forum/#!forum/geogebra-discovery).

## Feature matrix

### New features

This table is ordered by maturity.

| Feature | GeoGebra 	  | GeoGebra Discovery    | Maturity  |
|:-------	|:---------:	|:-------------------:	|:---------: |
| Discover tool/command	| no | [yes](https://matek.hu/zoltan/blog-20201019.php)	| ![stable](images/green.png) |
| Stepwise discovery	| no | [yes](https://matek.hu/zoltan/stepwise/csgg.pdf) | ![stable](images/green.png) |
| Compare command | no | [yes](https://matek.hu/zoltan/blog-20210125.php) | ![stable](images/green.png) |
| Proving inequalities | no | [yes](https://matek.hu/zoltan/blog-20211028.php) | ![stable](images/green.png) |
| RealQuantifierElimination command | no | [yes](https://matek.hu/zoltan/demo-20211118.php) | ![stable](images/green.png) |
| Prenex formulas | no | [yes](https://matek.hu/zoltan/blog-20220212.php) | ![stable](images/green.png) |
| IncircleCenter command | no	| [yes (with prover support)](https://matek.hu/zoltan/blog-20200929.php) | ![stable](images/green.png) |
| Incircle tool | no	| [yes](https://matek.hu/zoltan/blog-20200929.php) | ![stable](images/green.png) |
| IncircleCenter tool | no	| [yes](https://matek.hu/zoltan/blog-20200929.php) | ![stable](images/green.png) |
| LocusEquation	tool | no | yes	| ![stable](images/green.png) |
| Dilate command | only numerical | [with prover support](https://github.com/kovzol/geogebra/releases/tag/v5.0.641.0-2023Feb01) | ![stable](images/green.png) |
| Envelope tool | no	| [yes](https://matek.hu/zoltan/blog-20201111.php) | ![stable](images/green.png) |
| Raspberry Pi 3D View | no | yes | ![stable](images/green.png) |
| Giac: threads on Linux | no | yes | ![stable](images/green.png) |
| Same color for circles with the same radius | no | yes | ![stable](images/green.png) |
| Plotting logical connectives of inequalities | partial | [full](https://github.com/kovzol/geogebra/releases/tag/v5.0.641.0-2023Apr22) | ![unstable](images/orange.png) Possible errors on saving |
| Plot2D command | no | [yes](https://github.com/kovzol/geogebra/releases/tag/v5.0.641.0-2023Apr22) | ![unstable](images/orange.png) Possible errors on saving |
| CNI prover | no | [yes](https://github.com/kovzol/geogebra/releases/tag/v5.0.641.0-2025Nov01) | ![work in progress](images/wip.png) Subscripted labels yet unsupported |
| ShowProof command | no | [yes](https://github.com/kovzol/geogebra/releases/tag/v5.0.641.0-2024Apr15) | ![work in progress](images/wip.png) Translations missing |
| Export CAS View | no | [HTML, Mathematica, Maple and Giac](https://github.com/kovzol/geogebra/releases/tag/v5.0.641.0-2024Apr15) | ![work in progress](images/wip.png) Several commands missing |
| Export Construction Protocol as LaTeX | no | prototype | ![prototype](images/red.png) Working prototype |
| Automatic LaTeX captions | no | [prototype](https://github.com/kovzol/geogebra/releases/tag/v5.0.641.0-2023Oct06) | ![prototype](images/red.png) Support required for the web version |
| ApplyMap command | no | [prototype](https://matek.hu/zoltan/blog-20210126.php) | ![prototype](images/red.png) Bugs [1](https://geogebra-prover.myjetbrains.com/youtrack/issue/TP-60), [2](https://geogebra-prover.myjetbrains.com/youtrack/issue/TP-58) |

### Features that have already been merged

| Feature | GeoGebra version | Date |
|:------- |:--------------------: |:---: |
| Java OpenGL 2.5 support | 5.2 | September 2023 |
| [Fast symbolic angle bisectors (prover)](https://matek.hu/zoltan/blog-20200929.php) | 5.0.641.0 | May 2021 |
| [Algebraic curves as inputs in locus computations](https://matek.hu/zoltan/blog-20201031.php) |  5.0.641.0 | May 2021 |
| [Incircle (prover support)](https://matek.hu/zoltan/blog-20200929.php) | 5.0.641.0 | May 2021 |

### [Technical documentation](docs/technical.md)

We maintain a technical documentation to keep some programming related details up-to-date in order to help a possible merge of the two codebases.

## Bugs

The database of issues is available at [YouTrack](https://geogebra-prover.myjetbrains.com/youtrack/issues).

## Benchmarks
The [benchmarking system](https://prover-test.risc.jku.at/) collects results and speed related information on a daily basis for the [Prove](https://wiki.geogebra.org/en/Prove_Command), [ProveDetails](https://wiki.geogebra.org/en/Prove_Command), [LocusEquation](https://wiki.geogebra.org/en/LocusEquation_Command), [Envelope](https://wiki.geogebra.org/en/Envelope_Command) and Compare commands.

### Latest outputs
* [Prove/ProveDetails test](https://prover-test.risc.jku.at/job/GeoGebra_Discovery-provertest/lastSuccessfulBuild/artifact/fork/geogebra/test/scripts/benchmark/prover/html/all.html)
* [LocusEquation/Envelope test](https://prover-test.risc.jku.at/job/GeoGebra_Discovery-art-plottertest/lastSuccessfulBuild/artifact/fork/geogebra/test/scripts/benchmark/art-plotter/html/all.html)
* [Compare test](https://prover-test.risc.jku.at/job/GeoGebra_Discovery-comparetest/lastSuccessfulBuild/artifact/fork/geogebra/test/scripts/benchmark/compare/html/all.html)
* [Discover test](https://prover-test.risc.jku.at/job/GeoGebra_Discovery-discovertest/)
* [Prove test (inequalities)](https://prover-test.risc.jku.at/job/GeoGebra_Discovery-proverrgtest/lastSuccessfulBuild/artifact/fork/geogebra/test/scripts/benchmark/prover-rg/html/all.html)
* [ShowProof test](https://prover-test.risc.jku.at/job/GeoGebra_Discovery-showprooftest/lastSuccessfulBuild/artifact/fork/geogebra/test/scripts/benchmark/prover/html/all.html)


### All outputs
* [Prove/ProveDetails test](https://prover-test.risc.jku.at/job/GeoGebra_Discovery-provertest/)
* [LocusEquation/Envelope test](https://prover-test.risc.jku.at/job/GeoGebra_Discovery-art-plottertest/)
* [Compare test](https://prover-test.risc.jku.at/job/GeoGebra_Discovery-comparetest/)
* [Discover test](https://prover-test.risc.jku.at/job/GeoGebra_Discovery-discovertest/)
* [Prove test (inequalities)](https://prover-test.risc.jku.at/job/GeoGebra_Discovery-proverrgtest/)
* [ShowProof test](https://prover-test.risc.jku.at/job/GeoGebra_Discovery-showprooftest/)


## References

* [Z. Kovács, T. Recio, M. P. Vélez: GeoGebra Discovery in Context (ADG 2021: Automated Deduction in Geometry, p. 141–147, 2021)](https://cgi.cse.unsw.edu.au/~eptcs/paper.cgi?ADG2021.16)
* [Z. Kovács, T. Recio, M. P. Vélez: Automated Reasoning Tools in GeoGebra Discovery (ACM Communications in Computer Algebra 55(2), p. 39–43, 2021)](https://dl.acm.org/doi/10.1145/3493492.3493495)
* [Z. Kovács, T. Recio, M. P. Vélez: Automated Reasoning Tools with GeoGebra: What Are They? What Are They Good For? (Mathematics Education in the Age of Artificial Intelligence, p. 23–44, 2022)](http://dx.doi.org/10.1007/978-3-030-86909-0_2)

### Discover command
* [F. Botana, Z. Kovács, T. Recio: Towards an Automated Geometer (AISC 2018: Artificial Intelligence and Symbolic Computation, p. 215–220, 2018)](https://link.springer.com/chapter/10.1007/978-3-319-99957-9_15)
* [Z. Kovács, J. H. Yu: Towards Automated Discovery of Geometrical Theorems in GeoGebra, 2020](https://arxiv.org/abs/2007.12447)
* [Z. Kovács, T. Recio: GeoGebra Reasoning Tools for Humans and for Automatons, 2020](https://www.researchgate.net/publication/347256855_GeoGebra_Reasoning_Tools_for_Humans_and_for_Automatons)
* [Z. Kovács: Discovering geometry via the Discover command in GeoGebra Discovery, REMATEC 16(37), p. 14–25, 2021](https://www.researchgate.net/publication/348598407_Discovering_geometry_via_the_Discover_command_in_GeoGebra_Discovery)
* [Z. Kovács, J. H. Yu: Stepwise discovery of mathematical knowledge in GeoGebra, 2022](https://www.researchgate.net/publication/367022755_Stepwise_discovery_of_mathematical_knowledge_in_GeoGebra)

### Relation command
* [Z. Kovács: The Relation Tool in GeoGebra 5 (ADG 2014: Automated Deduction in Geometry, p. 53–71, 2015)](https://link.springer.com/chapter/10.1007/978-3-319-21362-0_4)
* [A. Hota, Z. Kovács, A. Vujic: Solving Some Geometry Problems of the Náboj 2023 Contest with Automated Deduction in GeoGebra Discovery (ADG 2023: Automated Deduction in Geometry, p. 110–123, 2023)](https://cgi.cse.unsw.edu.au/~eptcs/paper.cgi?ADG2023.14)

### Prove/ProveDetails commands
* [F. Botana, M. Hohenwarter, P. Janičić, Z. Kovács, I. Petrović, T. Recio, S. Weitzhofer: Automated Theorem Proving in GeoGebra: Current Achievements (Journal of Automated Reasoning 55, p. 39–59, 2015)](https://link.springer.com/article/10.1007/s10817-015-9326-4)
* [Z. Kovács, T. Recio, M.P. Vélez: Detecting truth, just on parts (Revista Matemática Complutense 32, p. 451–474, 2018)](https://link.springer.com/article/10.1007/s13163-018-0286-1)
* [Z. Kovács, T. Recio, L.F. Tabera, M.P. Vélez: Dealing with Degeneracies in Automated Theorem Proving in Geometry (Mathematics 9.16, p. 1964, 2021)](https://www.mdpi.com/2227-7390/9/16/1964)

### Compare command
* [C. Abar, Z. Kovács, T. Recio, R. Vajda: Conectando Mathematica e GeoGebra para explorar construções geométricas planas, 2019](https://www.researchgate.net/publication/337499551_Conectando_Mathematica_e_GeoGebra_para_explorar_construcoes_geometricas_planas)
* [R. Vajda, Z. Kovács: GeoGebra and the realgeom Reasoning Tool, 2020](https://www.researchgate.net/publication/345246253_GeoGebra_and_the_realgeom_Reasoning_Tool)
* [C.W. Brown, Z. Kovács, R. Vajda: Supporting Proving and Discovering Geometric Inequalities in GeoGebra by using Tarski (ADG 2021: Automated Deduction in Geometry, p. 156–166, 2021)](https://cgi.cse.unsw.edu.au/~eptcs/paper.cgi?ADG2021.18)

### RealQuantifierElimination command
* [Z. Kovács, T. Recio: Real quantifier elimination in the classroom, 2022](https://www.researchgate.net/publication/366177699_Real_quantifier_elimination_in_the_classroom)

### ShowProof command
* [Z. Kovács, T. Recio, M. P. Vélez: Showing Proofs, Assessing Difficulty with GeoGebra Discovery (ADG 2023: Automated Deduction in Geometry, p. 43–52, 2023)](https://cgi.cse.unsw.edu.au/~eptcs/paper.cgi?ADG2023.8)

### Plot2D command
* [C. Brown, Z. Kovács, T. Recio: Faithful Real-Time Animation of Parametrized (Semi-) Algebraic Expressions via Cylindrical Algebraic Decomposition (ACM Commun. Comput. Algebra 57.2, p. 43-46, 2023)](https://doi.org/10.1145/3614408.3614413)

### LocusEquation command
* [Z. Kovács: Real-time Animated Dynamic Geometry in the Classrooms by Using Fast Gröbner Basis Computations (MCS 11, 351–361, 2017)](https://www.researchgate.net/publication/314403276_Real-time_Animated_Dynamic_Geometry_in_the_Classrooms_by_Using_Fast_Grobner_Basis_Computations)
* [A. Käferböck, Z. Kovács: The Locus Story of a Rocking Camel in a Medical Center in the City of Freistadt (ADG 2023: Automated Deduction in Geometry, p. 132–141, 2023)](https://cgi.cse.unsw.edu.au/~eptcs/paper.cgi?ADG2023.16)

### Envelope command
* [F. Botana, Z. Kovács: New tools in GeoGebra offering novel opportunities to teach loci and envelopes (arXiv 1605.09153, 2016)](https://www.researchgate.net/publication/303681352_New_tools_in_GeoGebra_offering_novel_opportunities_to_teach_loci_and_envelopes)
* [Z. Kovács: Achievements and Challenges in Automatic Locus and Envelope Animations in Dynamic Geometry (MCS 13(3), p. 131–141, 2019)](https://www.researchgate.net/publication/328912538_Achievements_and_Challenges_in_Automatic_Locus_and_Envelope_Animations_in_Dynamic_Geometry)
* [Z. Kovács: Easy (but exact) study of caustics of conics (eJMT 17(3), p. 185–205, 2023)](https://www.researchgate.net/publication/376721673_Easy_but_exact_study_of_caustics_of_conics)
