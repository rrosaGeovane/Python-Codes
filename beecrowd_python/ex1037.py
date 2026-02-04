#Você deve fazer um programa que leia um valor qualquer e
#apresente uma mensagem dizendo em qual dos seguintes intervalos
#([0,25], (25,50], (50,75], (75,100]) este valor se encontra.
#Obviamente se o valor não estiver em nenhum destes intervalos,
#deverá ser impressa a mensagem “Fora de intervalo”

a = list(range(0, 26))
b = list(range(26, 51))
c = list(range(51, 76))
d = list(range(76, 101))

print("Existem 4 intervalos, chamados de: A,B,C e D")

valor = int(input("Digite um valor para ver em qual intervalo ele se encontra: "))


if valor in a:
    print("O número se encontra dentro desse intervalo: [0, 25]")
elif valor in b:
    print("O número se encontra dentro desse intervalo: [25, 50]")
elif valor in c:
    print("O número se encontra dentro desse intervalo: [50, 75]")
elif valor in d:
    print("O número se encontra dentro desse intervalo: [75, 100]")
else:
    print("\033[1:31mO seu número não se encaixa em nenhum intervalo! :/\033[m")
