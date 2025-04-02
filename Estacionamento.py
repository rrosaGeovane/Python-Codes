import re

print("Estacionamento")

placa = input("Digite sua placa ( AAA-9999 ): ").upper()
temp = float(input("tempo de permanÃªncia em horas: "))
preco = 0.00

if not re.match(r'^[A-Z]{3}-\d{4}$', placa):
    print("Placa invÃ¡lida! O formato deve ser AAA-9999.")
else:
    if temp <= 1:
        preco = 5.00
    elif 1 > temp <= 3:
        preco = 5.00 + (temp - 1)*4.00
    else:
        preco = 5.00 + 8.00 + (temp - 3) * 3
        
    print(f"O valor final, com {temp:.2f} hora(s) ficou: R${preco:.2f}")
    print(f"Placa do carro: {placa}")