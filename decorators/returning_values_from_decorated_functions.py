def mean(func):
    def wrapper(list_of_numbers):
        func(list_of_numbers)
        print("and also here's the mean:")
        sum = 0
        for n in list_of_numbers:
            sum += int(n)
        print(sum / len(list_of_numbers))
    return wrapper


@mean
def your_numbers(users_number):
    print("Here are your numbers:")
    print(users_number)


users_number = []
done = "no"

while done == "no":
    a_number = input("Enter you number or (x) to quit: ")
    if a_number == "x":
        break
    else:
        users_number.append(a_number)


your_numbers(users_number)
