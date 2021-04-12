# this is a terrible example, honestly. 

def sum(num1, num2):
    try:
        print("sum: ",int(num1)+int(num2))
    except:
        print("sum: there was an error!")

def better_sum(num1, num2):
    if isinstance(num1, int) and isinstance(num2, int):
        print("better_sum: ", num1 + num2)
    else:
        print("better_sum: entry was not a number!")


number1 = input("enter a number ")
sum(number1, 12)

number1 = int(input("enter a number "))
better_sum(number1, 12)
