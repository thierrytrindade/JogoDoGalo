
tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
linha = 0
coluna = 0

jogador1 = ["Maria", "X", "azul", 0]
jogador2 = ["João", "0", "vermelho", 0]

jogador_atual = 0
contador_jogadas = 0
resultado = 0
Empates = 0

modo_jogo = 0
total_jogos = 0
sinal_interrupcao  = 0


# Criação do tabuleiro como vetor unidimensional com 9 elementos
tabuleiro = [" "] * 9  # Cria uma lista com 9 espaços em branco

# Função para desenhar o tabuleiro em formato 3x3 usando o vetor
def desenhar_tabuleiro(tab):
    for i in range(3):
        # Mapeia os índices do vetor para as linhas: 0-2, 3-5, 6-8
        linha = " | ".join(tab[i*3:(i+1)*3])
        print(linha)
        if i < 2:
            print("--+---+--")

# Chamada da função para desenhar o tabuleiro
desenhar_tabuleiro(tabuleiro)