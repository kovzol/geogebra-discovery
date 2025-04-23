#!/usr/bin/python3

# Run this from GeoGebra's root folder to fix tool names.
# There was a big upstream change around summer 2024 that unified and improved these names.

import shutil
import subprocess

file_map = {
    "moverotate": "movearoundpoint",
    "orthogonal": "perpendicularline",
    "parallel": "parallelline",
    "linebisector": "perpendicularbisector",
    "angularbisector": "anglebisector",
    "compasses": "compass",
    "circlearc3": "circulararc3",
    "circlesector3": "circularsector3",
    "circumcirclearc3": "circumcirculararc3",
    "circumcirclesector3": "circumcircularsector3",
    "hyperbola3": "hyperbola",
    "ellipse3": "ellipse",
    "createlist": "list",
    "mirroratplane": "reflectatplane",
    "mirroratpoint": "reflectatpoint",
    "mirroratline": "reflectatline",
    "mirroratcircle": "reflectatcircle",
    "rotatebyangle": "rotatearoundpoint",
    "buttonaction": "button",
    "showcheckbox": "checkbox",
    "textfieldaction": "inputbox",
    "translateview": "movegraphicsview"
}

folders_svg = ["common/src/nonfree/resources/org/geogebra/common/icons/svg/web/toolIcons"]

folders_png = ["common/src/nonfree/resources/org/geogebra/common/icons_toolbar/p32/",
    "common/src/nonfree/resources/org/geogebra/common/icons_toolbar/p64/"]

def copy(file_map, folders, ext):
    for src, dst in file_map.items():
        for f in folders:
            try:
                shutil.copy(f + "/mode_" + src + ext, f + "/mode_" + dst + ext)
                print(f"Successfully copied: {src} → {dst}")
                subprocess.run(["git", "add", f + "/mode_" + dst + ext]) 
            except FileNotFoundError:
                print(f"Error: '{f}/{src}{ext}' cannot be found.")
            except Exception as e:
                print(f"Error during copying '{f}/{src}{ext}': {e}")

if __name__ == "__main__":
    copy(file_map, folders_svg, ".svg")
    copy(file_map, folders_png, ".png")
