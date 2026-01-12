menu = """

[d] Deposit
[w] Withdraw
[s] Statement
[q] Quit

=> """
balance = 0
limit_amount = 500
statement = ""
withdraw_count = 0
MAX_WITHDRAWS = 3


def deposit(balance, statement):
    amount = float(input("Enter deposit amount: "))

    if amount > 0:
        balance += amount
        statement += f"Deposit: $ {amount:.2f}\n"
        return balance, statement, "Deposit successful!"
    else:
        return balance, statement, "Operation failed! Invalid amount."


def withdraw(balance, withdraw_count, statement, limit_amount, MAX_WITHDRAWS):
    amount = float(input("Enter withdrawal amount: "))

    if amount > balance:
        return balance, withdraw_count, statement, "Operation failed! Insufficient funds."
    elif amount > limit_amount:
        return balance, withdraw_count, statement, "Operation failed! Withdrawal exceeds limit."
    elif withdraw_count >= MAX_WITHDRAWS:
        return balance, withdraw_count, statement, "Operation failed! Maximum withdrawals reached."
    elif amount > 0:
        balance -= amount
        statement += f"Withdrawal: $ {amount:.2f}\n"
        withdraw_count += 1
        return balance, withdraw_count, statement, "Withdrawal successful!"
    else:
        return balance, withdraw_count, statement, "Operation failed! Invalid amount."


def show_statement(balance, statement):
    print("\n================ STATEMENT ================")
    print("No transactions made." if not statement else statement)
    print(f"\nBalance: $ {balance:.2f}")
    print("===========================================")


def error_message():
    return "Invalid operation. Please select a valid option."


while True:
    option = input(menu)

    if option == "d":
        balance, statement, message = deposit(balance, statement)
        print(message)

    elif option == "w":
        balance, withdraw_count, statement, message = withdraw(
            balance, withdraw_count, statement, limit_amount, MAX_WITHDRAWS
        )
        print(message)

    elif option == "s":
        show_statement(balance, statement)

    elif option == "q":
        break

    else:
        print(error_message())
