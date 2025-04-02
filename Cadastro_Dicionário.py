from time import sleep

nome = ""
idade = id = 0

cadastros = {}

while True:
    print("Cadastros\n"
          "[ 1 ]Adicionar cadastro\n"
          "[ 2 ]Remover cadastro\n"
          "[ 3 ]Apresentar os nomes cadastrados em ordem alfabética\n"
          "[ 4 ]Sair do programa")
    resp = int(input("Sua opção: "))
    print()

    if resp not in[1,2,3,4]:
        print("\033[1:31mNúmeros inválidos\033[m")
        print()
        sleep(2)

    elif resp == 4:
        break

    elif resp == 1:
        id = int(input("Digite a matrícula do usuário: "))
        nome = input("Digite o nome do usuário: ").strip()
        idade = int(input("Digite a idade: "))

        if id in cadastros:
            print("\033[1:31mUsuário já cadastrado!\033[m")
            print()
            sleep(2)
            continue
        else:
            cadastros[id] = {
                "nome": nome,
                "idade": idade
            }
        print("\033[1:32mUsuário cadastrado com sucesso\033[m")
        print()
        sleep(2)


    elif resp == 2:
        id = int(input("Digite a matrícula a ser excluída: "))
        if id in cadastros:
            del cadastros[id]
            print("\033[1:32mUsuário Removido com Sucesso!\033[m")
            print()
            sleep(2)
        else:
            print("\033[1:31mUsuário não existe.\033[m")
            print()
            sleep(2)

    else:
        if not cadastros:
            print("CADASTROS: ")
            print("\033[1:31mNenhum usuário cadastrado!\033[m")
            print()
            sleep(2)
        else:
            print("CADASTROS: ")
            cadastros_organizados = sorted(cadastros.items(), key=lambda item: item[1]["nome"])
            for id, dados in cadastros_organizados:
                print(f"Matrícula: {id}\nNome: {dados['nome']}\nIdade: {dados['idade']}\n" + "-" * 30)
            print()
            sleep(2)

