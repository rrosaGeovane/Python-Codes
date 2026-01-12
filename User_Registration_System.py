from time import sleep

name = ""
age = user_id = 0

registrations = {}

while True:
    print(
        "Registrations\n"
        "[ 1 ] Add registration\n"
        "[ 2 ] Remove registration\n"
        "[ 3 ] Show registered names in alphabetical order\n"
        "[ 4 ] Exit program"
    )

    choice = int(input("Your choice: "))
    print()

    if choice not in [1, 2, 3, 4]:
        print("\033[1:31mInvalid option\033[m")
        print()
        sleep(2)

    elif choice == 4:
        break

    elif choice == 1:
        user_id = int(input("Enter user ID: "))
        name = input("Enter user name: ").strip()
        age = int(input("Enter age: "))

        if user_id in registrations:
            print("\033[1:31mUser already registered!\033[m")
            print()
            sleep(2)
            continue
        else:
            registrations[user_id] = {
                "name": name,
                "age": age
            }

        print("\033[1:32mUser successfully registered\033[m")
        print()
        sleep(2)

    elif choice == 2:
        user_id = int(input("Enter ID to remove: "))
        if user_id in registrations:
            del registrations[user_id]
            print("\033[1:32mUser removed successfully!\033[m")
            print()
            sleep(2)
        else:
            print("\033[1:31mUser does not exist.\033[m")
            print()
            sleep(2)

    else:
        if not registrations:
            print("REGISTRATIONS:")
            print("\033[1:31mNo users registered!\033[m")
            print()
            sleep(2)
        else:
            print("REGISTRATIONS:")
            sorted_registrations = sorted(
                registrations.items(),
                key=lambda item: item[1]["name"]
            )

            for user_id, data in sorted_registrations:
                print(
                    f"ID: {user_id}\n"
                    f"Name: {data['name']}\n"
                    f"Age: {data['age']}\n"
                    + "-" * 30
                )
            print()
            sleep(2)
