try:
    with open('sample.txt', mode='r') as my_file:
        print(my_file.read())
        result = 2 + '2'
except FileNotFoundError:
    print("file does not exist: FileNotFoundError")
except TypeError:
    print("there was a type error!")
except:
    print("something else went wrong, sorry.")
finally:
    print("so, we're done.")


print("but this line was run ... ")
