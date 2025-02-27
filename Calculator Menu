import time

num1 = float(input("Enter the 1st value: "))
num2 = float(input("Enter the 2nd value: "))

option = 0

while option != 5:
    print("[ 1 ] Add\n"
          "[ 2 ] Multiply\n"
          "[ 3 ] Greater")
    print("[ 4 ] New Numbers\n"
          "[ 5 ] Exit Program\n"
          "[ 6 ] Division")
    
    option = int(input("What is your choice? "))
    
    if option == 1:
        sum_result = num1 + num2
        print(f"The sum of {num1:.2f} and {num2:.2f} is = {sum_result:.2f}")
        print("=-=" * 10)
        print("\n")
        time.sleep(3)
    
    elif option == 2:
        multiplication = num1 * num2
        print(f"The multiplication of {num1:.2f} and {num2:.2f} is = {multiplication:.2f}")
        print("=-=" * 10)
        print("\n")
        time.sleep(3)
    
    elif option == 3:
        if num1 > num2:
            print(f"The greater number is: {num1:.2f}")
        else:
            print(f"The greater number is: {num2:.2f}")
        print("=-=" * 10)
        print("\n")
        time.sleep(3)
    
    elif option == 4:
        num1 = float(input("Enter the 1st value: "))
        num2 = float(input("Enter the 2nd value: "))
        print("=-=" * 10)
        print("\n")
        time.sleep(3)
    
    elif option == 6:
        division = num1 / num2
        print(f"{num1:.2f} / {num2:.2f} = {division:.2f}")
        print("=-=" * 10)
        print("\n")
        time.sleep(3)
    
    elif option > 6:
        print("\033[1;31mError! Try again\033[m")
        print("=-=" * 10)
        print("\n")
        time.sleep(3)
    
    else:
        print("Exiting...")
        print("=-=" * 10)
        print("\n")
        time.sleep(2)
