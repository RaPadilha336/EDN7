import statistics

def ler_log_e_analisar(caminho_arquivo):
    tempos_execucao = []

    try:
        with open(caminho_arquivo, 'r') as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if linha:
                    try:
                        tempo = float(linha)
                        tempos_execucao.append(tempo)
                    except ValueError:
                        print(f"Ignorando linha inválida: {linha}")

        if tempos_execucao:
            media = statistics.mean(tempos_execucao)
            desvio_padrao = statistics.stdev(tempos_execucao)
            print(f"Média do tempo de execução: {media:.2f} segundos")
            print(f"Desvio padrão: {desvio_padrao:.2f} segundos")
        else:
            print("Nenhum dado válido encontrado no arquivo.")

    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho_arquivo}")

# Exemplo de uso
ler_log_e_analisar('dados/log_treinamento.txt')
