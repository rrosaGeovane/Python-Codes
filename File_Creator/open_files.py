import os
import pandas as pd
from time import sleep
from colors import *

def criar(caminho):
    validacao = False
    while True:
        try:
            quant = int(input("Digite a quantidade de Pastas: "))
            if quant == 0:
                print(purple("O usuário decidiu não criar nenhuma pasta"))
                return 0
        except ValueError:
            print(red("Entrada inválida!"))
            sleep(1)
        else:
            for c in range(quant):
                nome_da_pasta = input(f"Nome da {c+1}º pasta: ")
                caminho_completo = os.path.join(caminho, nome_da_pasta)
                os.makedirs(caminho_completo, exist_ok=True)
                while True:
                    try:
                        qtd_sub = int(input(f"Digite a quantidade de Subpastas da Pasta: {nome_da_pasta}: "))
                    except ValueError:
                        print(red("Entrada inválida!"))
                        sleep(1)
                    else:
                        for i in range(qtd_sub):
                            sub = input(f"Nome da {i+1}º subpasta da pasta {nome_da_pasta}: ")
                            os.makedirs(os.path.join(caminho_completo, sub), exist_ok=True)
                        print(green(f"Subpastas de {nome_da_pasta} criadas com SUCESSO!"))
                        break
            print(green("Pastas Criadas com Sucesso!"))
            break

criar(caminho = "E:/OneDrive/Documentos")


"""def criar_com_planilha(caminho, planilha):
    nome_da_pasta = input(f"Nome da pasta: ")
    caminho_completo = os.path.join(caminho, nome_da_pasta)
    os.makedirs(caminho_completo, exist_ok=True)

    for i in range(qtd_sub):
        sub = input(f"Nome da {i}º subpasta da pasta {nome_da_pasta}: ")
        os.makedirs(os.path.join(caminho_completo, sub), exist_ok=True)"""

