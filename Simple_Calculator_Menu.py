import time

num1 = float(input("Enter the 1st value: "))
num2 = float(input("Enter the 2nd value: "))

option = 0

while option != 5:
    print(
        "[ 1 ] Add\n"
        "[ 2 ] Multiply\n"
        "[ 3 ] Greater\n"
        "[ 4 ] New Numbers\n"
        "[ 5 ] Exit Program\n"
        "[ 6 ] Division"
    )

    option = int(input("What is your choice? "))

    if option == 1:
        result = num1 + num2
        print(f"The sum of {num1:.2f} and {num2:.2f} is = {result:.2f}")

    elif option == 2:
        result = num1 * num2
        print(f"The multiplication of {num1:.2f} and {num2:.2f} is = {result:.2f}")

    elif option == 3:
        greater = num1 if num1 > num2 else num2
        print(f"The greater number is: {greater:.2f}")

    elif option == 4:
        num1 = float(input("Enter the 1st value: "))
        num2 = float(input("Enter the 2nd value: "))

    elif option == 6:
        result = num1 / num2
        print(f"{num1:.2f} / {num2:.2f} = {result:.2f}")

    elif option > 6:
        print("\033[1;31mError! Try again\033[m")

    else:
        print("Exiting...")

    print("=-=" * 10, "\n")
    time.sleep(2)
