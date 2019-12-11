import glob
mp3_files = glob.glob('**/*.mp3', recursive=True)
f = open("filenamesinfolder.txt", "w+", encoding="utf-8")
for filename in mp3_files:
    f.write(filename[:-4] + "\n")
f.close()