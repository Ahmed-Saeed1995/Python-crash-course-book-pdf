while True:
    try:
        number1 = int(input("Enter a number 1 to add:\n"))
        number2 = int(input("Enter a number 2 to add:\n"))
        result = number1 + number2
    except ValueError:
        print("You can`t add tow string togther as numbers")
    else:
        print(result)
