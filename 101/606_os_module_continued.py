import os


for dirpath, dirnames, filenames in os.walk("myfolder"):
    # print(dirpath, dirnames, filenames, sep="\n")
    # print("---------------")
    pass

print(os.environ.get("HOME"))
print(os.environ.get("HOME")+"/"+"madeupfile.txt", sep='')

print(os.path.join(os.environ.get("HOME"), "anothermadeupfile.txt"))

# get the basename or filename
print("basename: ", os.path.basename("/some/dir/thisfile.txt"))
# get directory name
print("dirname:  ", os.path.dirname("some/dir/thisfile.txt"))
# get tuple of directory name and basename
print("split:    ", os.path.split("/some/dir/thisfile.txt"))

os.path.exists("/some/dir/thisfile.txt")
os.path.isdir("path/file.end")
os.path.isfile("somepath/somefilename.md")


# splits off path and filename from extension
print(os.path.splitext("somepath/somefilename.md"))
print(os.path.splitext(os.path.basename("/some/dir/thisfile.txt")))

print(os.path.join("/äöö\\", "anothermadeupfile.txt"))
print(os.path.join("anothermadeupfile.txt/", "/asdfasd\\"))
