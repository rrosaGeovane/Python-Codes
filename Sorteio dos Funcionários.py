import os
import random
 
PASTA_RAIZ = 'Dados dos funcionários'
ARQUIVO_SAIDA = 'todos_funcionarios.txt'
 
 
def coletar_nomes():
    todos_nomes = []
 
    for i in range(1, 41):
        nome_pasta = f'setor{i}'
        caminho_pasta = os.path.join(PASTA_RAIZ, nome_pasta)
        arquivo_cadastro = os.path.join(caminho_pasta, 'cadastros.txt')
 
        try:
            with open(arquivo_cadastro, 'r', encoding='utf-8') as f:
                nomes = [linha.strip() for linha in f if linha.strip()]
                todos_nomes.extend(nomes)
                print(f'✅ {len(nomes)} nomes lidos do {nome_pasta}')
        except FileNotFoundError:
            print(f'⚠️ Arquivo não encontrado em {nome_pasta}')
        except Exception as e:
            print(f'❌ Erro no {nome_pasta}: {str(e)}')
 
    return todos_nomes
 
 
def salvar_nomes(nomes):
    with open(ARQUIVO_SAIDA, 'w', encoding='utf-8') as f:
        f.write('\n'.join(nomes))
    print(f'\n📁 Todos os nomes foram salvos em "{ARQUIVO_SAIDA}"')
 
 
def sortear_ganhador(nomes):
    if not nomes:
        print('Nenhum nome encontrado para sorteio!')
        return None
 
    ganhador = random.choice(nomes)
    print('\n🎉🎊 SORTEIO REALIZADO 🎊🎉')
    print(f'PARABÉNS AO GANHADOR(A): {ganhador}')
    return ganhador
 
 
if __name__ == '__main__':
    print('Iniciando processamento...\n')
    nomes_funcionarios = coletar_nomes()
 
    if nomes_funcionarios:
        salvar_nomes(nomes_funcionarios)
        sortear_ganhador(nomes_funcionarios)
    else:
        print('Nenhum nome de funcionário foi encontrado!')
