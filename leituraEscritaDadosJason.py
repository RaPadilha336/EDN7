import json

def escrever_json(caminho_arquivo, dados):
    try:
        with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo_json:
            json.dump(dados, arquivo_json, ensure_ascii=False, indent=4)
        print(f"Dados escritos com sucesso em '{caminho_arquivo}'.")
    except Exception as e:
        print(f"Erro ao escrever o arquivo JSON: {e}")

def ler_json(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo_json:
            dados = json.load(arquivo_json)
            print("Dados lidos do arquivo JSON:\n")
            print(f"Nome: {dados['nome']}")
            print(f"Idade: {dados['idade']}")
            print(f"Cidade: {dados['cidade']}")
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho_arquivo}")
    except Exception as e:
        print(f"Erro ao ler o arquivo JSON: {e}")

# Exemplo de dados
dados_pessoa = {
    'nome': 'João Silva',
    'idade': 30,
    'cidade': 'Curitiba'
}

# Caminho do arquivo
caminho = 'dados/pessoa.json'

# Executando as funções
escrever_json(caminho, dados_pessoa)
ler_json(caminho)
