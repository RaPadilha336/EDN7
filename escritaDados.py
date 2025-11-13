import csv

def escrever_dados_csv(caminho_arquivo, dados):
    with open(caminho_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
        escritor = csv.DictWriter(arquivo_csv, fieldnames=['Nome', 'Idade', 'Cidade'])
        escritor.writeheader()
        for pessoa in dados:
            escritor.writerow(pessoa)
    print(f"Arquivo CSV '{caminho_arquivo}' criado com sucesso.")

# Exemplo de dados
dados_pessoais = [
    {'Nome': 'Ana Souza', 'Idade': 28, 'Cidade': 'São Paulo'},
    {'Nome': 'Carlos Lima', 'Idade': 35, 'Cidade': 'Rio de Janeiro'},
    {'Nome': 'Beatriz Rocha', 'Idade': 22, 'Cidade': 'Belo Horizonte'}
]

# Executando a função
escrever_dados_csv('dados/pessoas.csv', dados_pessoais)
