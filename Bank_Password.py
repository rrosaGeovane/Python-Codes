password = "485932"
attempts = hint = 0

print("PYTHON BANK")

while attempts < 5:
    user_input = input("Enter the bank password: ")

    if user_input == password:
        print("\033[1:32mPassword accepted\033[m, Welcome!!")
        break
    else:
        attempts += 1
        hint = ""
        for i in range(len(password)):
            if i < len(user_input) and user_input[i] == password[i]:
                hint += password[i]
            else:
                hint += "*"

    print(f"\033[1:31mWrong password!\033[m Try again. Hint: {hint}")

    if attempts == 5:
        print("\033[1:31mYou exceeded the number of attempts. Try again later\033[m")
