import random

def password_generator(characters):
    char_list = list(characters)
    random.shuffle(char_list)

    size = int(input("Enter password length (MAXIMUM 67 CHARACTERS): "))

    if size < 5:
        print("Password too short! Minimum 5 characters.")
    else:
        for i in range(size):
            print(char_list[i], end="")


options = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%&"

password_generator(options)
