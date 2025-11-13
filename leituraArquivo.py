import csv

def ler_dados_csv(caminho_arquivo):
    try:
        with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo_csv:
            leitor = csv.DictReader(arquivo_csv)
            print("Dados encontrados no arquivo CSV:\n")
            for linha in leitor:
                nome = linha['Nome']
                idade = linha['Idade']
                cidade = linha['Cidade']
                print(f"Nome: {nome}, Idade: {idade}, Cidade: {cidade}")
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho_arquivo}")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")

# Exemplo de uso
ler_dados_csv('dados/pessoas.csv')
