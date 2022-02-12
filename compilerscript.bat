@echo off
pyinstaller --noconfirm --onefile --distpath "./windows" --windowed --icon "./textures/Player_1.ico" --add-data "./convpictolvl.py;." --add-data "./versioncontrol.py;." --add-data "./draw.py;." --add-data "./level.py;." --add-data "./player.py;." --add-data "./textures;textures/" --add-data "./Levels;Levels/" --add-data "./Levelpictures;Levelpictures/" --add-data "./backgroundmusic;backgroundmusic/"  "./main.py"
echo "File can be found in ./windows"
