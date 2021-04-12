import os

print(os.getcwd())              # pwd (current working directory)

os.chdir("/Users/alex/")        # cd
print(os.getcwd())

print(os.listdir())             # ls (list of items in directory)

if "myfoldertoday" not in os.listdir():
    os.mkdir("myfoldertoday")   # mkdir
else:
    print("myfoldertoday already exists")

os.makedirs("myfoldertoday/subfolder/datafolder")
                                # mkdir -p

os.remove("myfoldertoday/subfolder/datafolder/file.txt")
                                # delete specific file
os.rmdir("myfoldertoday/subfolder/datafolder")
                                # delete specific folder

os.removedirs("myfoldertoday/subfolder")
                                # handle with care, removes whole directory tree

os.rename("myfoldertoday/subfolder/datafolder/file.txt", "myfoldertoday/subfolder/datafolder/file2.txt")
                                # rename file
