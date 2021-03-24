x = 0
while x < 10:
    print(x, end=" - x - ")

    # x = x + 1
    x += 3

    if x == 6:
        continue

    print(x)

else:
    print("x is not less than 10 anymore")



y = 0
while y <= 10:
    print(y, end=" - y \n")
    y += 1
else:
    print('finished')
