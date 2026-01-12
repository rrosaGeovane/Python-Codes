import re

print("Parking Lot")

license_plate = input("Enter your license plate (AAA-9999): ").upper()
time_hours = float(input("Parking time in hours: "))
price = 0.00

if not re.match(r'^[A-Z]{3}-\d{4}$', license_plate):
    print("Invalid license plate! Format must be AAA-9999.")
else:
    if time_hours <= 1:
        price = 5.00
    elif 1 < time_hours <= 3:
        price = 5.00 + (time_hours - 1) * 4.00
    else:
        price = 5.00 + 8.00 + (time_hours - 3) * 3.00

    print(f"Final price for {time_hours:.2f} hour(s): ${price:.2f}")
    print(f"Car license plate: {license_plate}")
