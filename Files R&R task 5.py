try:
    number = int(input("Please enter a number between 1 and 100: "))
    if  0 < number < 100:
        print(number)
    else:
        print("Please enter a number between 1 and 100")
except ValueError:
    print("The value entered was not a number")
