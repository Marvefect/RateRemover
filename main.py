import os
from os import listdir
import shutil
import platform

if platform.system() == "Windows":
    div = "\\"
    print("Detected Windows")
elif platform.system() == "Linux":
    div = "/"
    print("Detected Linux")
else:
    print("Unsupported OS! (MacOs Support Soon-ish TM)")
    n = int(input())
    exit()

print("Marvefect's Rate Remover \nMade for o!Lazer players")

print("Input Directory to take songs from: \nExample: C:\\Users\\user\\RateRemover\\Input\\")
dir_in = str(input())
print("Output Directory to put resulting songs in: \nExample: C:\\Users\\user\\RateRemover\\Output\\")
dir_out = str(input())
file_list = [f for f in listdir(dir_in)]
print("Found", len(file_list), "Files, \nWorking...")

for f in file_list:
    print(f)
    f_dir = dir_in + f
    f_out = dir_out + f + div
    shutil.unpack_archive(f_dir, f_out, "zip")
    mp3_files = [m for m in listdir(f_out) if m.endswith(".mp3")]
    m_file = min(mp3_files, key=len)
    for m in mp3_files:
        if m != m_file:
            os.remove(f_out + m)
    o_files = [o for o in listdir(f_out) if o.endswith(".osu")]
    for o in o_files:
        result = open(f_out + o, 'r').read(100).find(m_file)
        if result == -1:
            os.remove(f_out + o)
    shutil.make_archive(dir_out + f, "zip", f_out)
    os.remove(f_dir)
    shutil.rmtree(f_out)
    os.rename(dir_out + f + ".zip", dir_out + f)
print("Done")
n = int(input()) 
