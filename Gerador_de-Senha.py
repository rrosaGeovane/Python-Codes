import random
def gerador_senha(x):
    lista = list(x)
    random.shuffle(lista)
    size = int(input("Digite o tamanho da senha (MÁXIMO 67 CARACTERES): "))
    if size<5:
        print("Senha Curta!! Mínimo 5 caracteres")
    else:
        for c in range(size):
            print(lista[c], end="")

options = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%&"

gerador_senha(options)
