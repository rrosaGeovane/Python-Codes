def rule_of_three(Xi, Yi, Y):
    multiplication = Xi * Y
    result = multiplication / Yi
    return result


MENU = """RULE OF THREE
Xi-------Yi
X--------Y"""


print(MENU)
print("Enter the values of Xi, Yi, and Y respectively: ")
a = float(input())
b = float(input())
c = float(input())

print(f"{rule_of_three(a, b, c):.2f}")
