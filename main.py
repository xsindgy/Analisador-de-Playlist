import pandas as pd
import os
from funcoes import tempo_total_em_h, tabela_albums, artistas_presentes, exportar_pdf


def mensagem_inicial():
    print('''Ola, seja bem-vindo(a)!
Primeiramente, muito obrigado por usar meu codigo!
Para usa-lo da melhor maneira, siga as instrucoes abaixo:
  1. Os dados da playlist devem estar obrigatoriamente em arquivo .CSV.
  2. Para obter os dados da sua playlist desejada em .CSV, acesse o site (https://exportify.net/).
  3. Copie o caminho do arquivo e cole logo abaixo:''', flush=True)


def limpar_terminal_keypress():
    input("\n--- Pressione Enter para continuar... ---")
    os.system('cls' if os.name == 'nt' else 'clear')


def carregar_arquivo():
    while True:
        arquivo = input('Digite o caminho do arquivo CSV (ex: playlist.csv): ')
        try:
            df = pd.read_csv(arquivo)
            print('Arquivo carregado com sucesso!')
            return df
        except (FileNotFoundError, OSError):
            print('Arquivo nao encontrado, por favor tente novamente!')


def renomear_colunas(df):
    return df.rename(columns={
        'Album Name': 'Álbum',   
        'Artist Name(s)': 'Artista(s)',
        'Genres': 'Gênero(s)'      
    })


def selecionar_acao_desejada(df):
    while True:
        print('''
Selecione a opcao desejada:

  1. Exibir a duracao total da playlist em horas
  2. Exibir artistas mais presentes na sua playlist
  3. Exibir albums mais presentes na sua playlist
  4. Exportar relatorio completo em PDF
  5. Finalizar app
''')
        entrada = input('Digite o numero da opcao desejada: ')

        if not entrada.strip().isdigit():
            print('Opcao invalida! Digite apenas o numero da opcao.')
            continue

        opcao = int(entrada)

        if opcao == 1:
            tempo_total_em_h(df)
        elif opcao == 2:
            artistas_presentes(df)
        elif opcao == 3:
            tabela_albums(df)
        elif opcao == 4:
            exportar_pdf(df)
        elif opcao == 5:
            print('Encerrando o app. Ate mais!')
            break
        else:
            print('Opcao invalida! Escolha entre 1 e 5.')
            continue

        print('''
O que deseja fazer agora?
  1. Voltar ao menu
  2. Finalizar app
''')
        opcao2 = input('Digite o numero da opcao desejada: ').strip()

        if opcao2 == '1':
            continue
        else:
            print('Encerrando o app. Ate mais!')
            break



mensagem_inicial()
limpar_terminal_keypress()

df = carregar_arquivo()
df = renomear_colunas(df)

selecionar_acao_desejada(df)


