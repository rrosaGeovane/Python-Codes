#Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara.
#Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”
#Caso haja uma divisão por 0 ou raiz de numero negativo.

a=float(input())
b=float(input())
c=float(input())

if a==0 or b==0 or c==0:
    print("\033[1:031mERRO")
else:
    delta = b ** 2 - 4 * a * c
    if delta<0:
        print("\033[1:031mNão tem raízes reais\033[30n!")
    else:
        x1 = (-b - delta**0.5) / (2 * a)
        x2 = (-b + delta**0.5) / (2 * a)
        print(f"As raízes são: x1={x1:.2f} e x2={x2:.2f}")
