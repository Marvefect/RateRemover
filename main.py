import os
from os import listdir
import shutil
import platform
import time
import threading

def OS():
    if platform.system() == "Windows":  return "\\"
    elif platform.system() == "Linux":  return "/"
    else: print("OS Unsupported."); n - int(input)

def Purge(dir_in, dir_out, f):
    print(f)
    f_dir = dir_in + f
    f_out = dir_out + f + div
    if f.endswith(".osz"):
        shutil.unpack_archive(f_dir, f_out, "zip")
        os.remove(f_dir)
    else:
        shutil.copytree(f_dir, f_out)
        shutil.rmtree(f_dir + div)
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
    shutil.rmtree(f_out)
    os.rename(dir_out + f + ".zip", dir_out + f)

if __name__ == "__main__":
    print("Marvefect's Rate Remover \nMade for o!Lazer players")
    div = OS()
    print("Input Directory to take songs from: \nExample: C:\\Users\\user\\RateRemover\\Input\\")
    dir_in = str(input())
    print("Output Directory to put resulting songs in: \nExample: C:\\Users\\user\\RateRemover\\Output\\")
    dir_out = str(input())
    start = time.time()
    for f in listdir(dir_in):
        thread = threading.Thread(target=Purge, args=(dir_in, dir_out, f))
        thread.start()
    thread.join()
    end = time.time()
    print("Done! Time taken: ", (end-start) * 10**3, "ms")
