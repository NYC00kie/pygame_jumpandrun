#!/usr/bin/env bash
pyver=$(python3 --version)
echo "Now Compiling Game with pyinstaller on Python Version $pyver"
pyinstaller --noconfirm --onefile --windowed --icon "./textures/Player_1.ico" --add-data "./convpictolvl.py;." --add-data "./draw.py;." --add-data "./level.py;." --add-data "./player.py;." --add-data "./textures;textures/" --add-data "./Levels;Levels/" --add-data "./Levelpictures;Levelpictures/" --add-data "./backgroundmusic;backgroundmusic/"  "./main.py"
echo "compilation complete"
echo "The Executable should now be in ./dist"
