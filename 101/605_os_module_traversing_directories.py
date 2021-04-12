import os


for dirpath, dirnames, filenames in os.walk("myfolder"):
    print(dirpath, dirnames, filenames, sep="\n")
    print("---------------")
