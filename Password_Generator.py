import random

def password_generator(size):
    
    total = "!@#$%&+-*/abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = "1234567890"
    symbol = "!@#$%&+-*/"
    
    if size < 8:
        return "Password too short! Minimum 8 characters."
    else:
        p = [
            random.choice(upper),
            random.choice(num),
            random.choice(symbol),
            ]
        p += random.choices(total, k=size-3)
        random.shuffle(p)
        password = "".join(p)
        return password
    
size = int(input("Enter password length: "))
print(password_generator(size))
