#!/usr/bin/env bash
pyver=$(python3 --version)
echo "Now Compiling Game with pyinstaller on Python Version $pyver"
pyinstaller --noconfirm --onefile --console --icon "./textures/Player_1.ico" --add-data "./draw.py;." --add-data "./level.py;." --add-data "./player.py;." --add-data "./textures;textures/" --add-data "./Levelpictures;Levelpictures/" --add-data "./colorcodedmaps;colorcodedmaps/" --add-data "./backgroundmusic;backgroundmusic/"  "./main.py"
echo "compilation complete"
echo "The Executable should now be in ./dist"
