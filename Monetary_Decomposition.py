amount = round(float(input()), 2)

N100 = amount // 100
remainder = amount % 100

N50 = remainder // 50
remainder %= 50

N20 = remainder // 20
remainder %= 20

N10 = remainder // 10
remainder %= 10

N5 = remainder // 5
remainder %= 5

N2 = remainder // 2
remainder %= 2
remainder = round(remainder, 2)

M1 = remainder // 1
remainder %= 1

M05 = remainder // 0.50
remainder %= 0.50

M025 = remainder // 0.25
remainder %= 0.25

M010 = remainder // 0.10
remainder %= 0.10

M005 = round(remainder / 0.05)
remainder %= 0.05

M001 = round(remainder / 0.01)

print("BANKNOTES:")
print(f"{N100:.0f} banknote(s) of $100.00")
print(f"{N50:.0f} banknote(s) of $50.00")
print(f"{N20:.0f} banknote(s) of $20.00")
print(f"{N10:.0f} banknote(s) of $10.00")
print(f"{N5:.0f} banknote(s) of $5.00")
print(f"{N2:.0f} banknote(s) of $2.00")

print("COINS:")
print(f"{M1:.0f} coin(s) of $1.00")
print(f"{M05:.0f} coin(s) of $0.50")
print(f"{M025:.0f} coin(s) of $0.25")
print(f"{M010:.0f} coin(s) of $0.10")
print(f"{M005:.0f} coin(s) of $0.05")
print(f"{M001:.0f} coin(s) of $0.01")
