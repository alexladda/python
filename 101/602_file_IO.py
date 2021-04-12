myfile = open('sample.txt')

contents = myfile.read()
print(contents)

print("--------------")

data = myfile.read()
print(data)   # cursor is at the end of the file, so data is empty

print("--------------")

myfile.seek(0)
data = myfile.read()
print(data)

print("--------------")

myfile.seek(0)
contents_list = myfile.readlines()
print(contents_list)

print("--------------")

print("closing file")
myfile.close()

print("--------------")

with open('sample.txt', mode='w') as my_file:
    my_file.write("\nTHIS IS A SENCTENCE\n")
    print("appending file")
    # automatically opens and closes

print("--------------")

my_appended_file = open('sample.txt')
print(my_appended_file.read())
