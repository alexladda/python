for i in range(10):
    with open("602_file_{0}.txt".format(i), mode='w') as txt_file:
        txt_file.write("the numer is {0}\n".format(i))
