import pathlib as pl
import os
import shutil as sh

source = pl.Path("./Source")
dest = pl.Path("./Converted")
remove_dl = True

songs = []

for directory in os.listdir(dest):
    song_name = directory
    if "_" in song_name:
        song_name = song_name[3:]
    songs.append(song_name)
    if song_name != directory and remove_dl:
        os.rename(dest / directory, dest / song_name)


for item in os.listdir(source):
    if item.rfind(".") != -1:
        continue
    print("Processing", item)

    jtem = item.split("_")
    song_name = jtem[0]
    file_name = "base.ogg" if len(jtem) == 1 else (jtem[1] + ".aff")
    target = dest / song_name

    if not target.exists():
        os.mkdir(target)
    sh.copy2(source / item, target / file_name)
