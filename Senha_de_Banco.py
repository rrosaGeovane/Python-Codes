senha = "485932"
cont = dica = 0

print("BANCO PYTHON")

while cont<5:
    user = input("Digite a senha do banco: ")

    if user == senha:
        print("\033[1:32mSenha aceita\033[m, Seja bem vindo!!")
        break
    else:
        cont += 1
        dica = ""
        for c in range (len(senha)):
            if c < len(user) and user[c] == senha[c]:
                dica += senha[c]
            else:
                dica += "*"

    print(f"\033[1:31mSenha Errada!\033[m Tente Novamente. Dica:{dica}")

    if cont==5:
        print("\033[1:31mVocÃª excedeu as tentativas. Tente novamente mais tarde\033[m")