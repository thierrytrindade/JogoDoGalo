# Variáveis iniciais
PREDEFENIDO = ""
AMARELO = "\033[1;33m"   
AZUL = "\033[1;34m"      
BRANCO = "\033[1;37m"    
CIANO = "\033[0;36m"     
ROXO = "\033[1;35m"      
VERDE = "\033[1;32m"     
VERMELHO = "\033[1;31m"  
END = "\033[0m"  # Anula a formatação anterior

# Função para ler input não vazio
def inputVazio(mensagem):
    while True:
        valor = input(mensagem)
        if valor == "":
            print("Você não digitou nada! Por favor, insira um valor válido.")
        else:
            return valor

# Inicializa os jogadores (estrutura: [nome, símbolo, cor, pontuação])
def inicializaJogadores():
    return [
        ["Jogador 1", "X", PREDEFENIDO, 0],
        ["Jogador 2", "O", PREDEFENIDO, 0]
    ]

# Outras funções (resumo, criaTabuleiro, inicializaTabuleiro, etc.)
def resumo(nome1, nome2, vitorias1, vitorias2, empates):
    numeroDeJogos = vitorias1 + vitorias2 + empates
    print("\n--- Resumo de", numeroDeJogos, "Jogo(s) ---")
    if numeroDeJogos > 0:
        print(nome1, "têm", vitorias1, " vitória(s),", (vitorias1 / numeroDeJogos) * 100, "%")
        print(nome2, "têm", vitorias2, " vitória(s),", (vitorias2 / numeroDeJogos) * 100, "%")
        print("Empates:", empates, ",", (empates / numeroDeJogos) * 100, "%")    
    else:
        print("Nenhuma partida foi concluída!")

def criaTabuleiro(linha, coluna, valor):
    tabuleiro = []
    for i in range(linha):
        linhai = []
        for j in range(coluna):
            linhai.append(valor)
        tabuleiro.append(linhai)
    return tabuleiro

def inicializaTabuleiro(tabuleiro, linha, coluna, valor):
    for i in range(linha):
        for j in range(coluna):
            tabuleiro[i][j] = valor
    return tabuleiro

def mostraTabuleiro(tabuleiro, linha, coluna):
    for i in range(linha):
        for j in range(coluna):
            print(tabuleiro[i][j], end=' ')
        print()

# Função que verifica se há vencedor (linhas, colunas e diagonais)
def verificaVencedor(tabuleiro, simbolo):
    for i in range(3):
        if (tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == simbolo) or (tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == simbolo):
            return True
    if (tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == simbolo) or (tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == simbolo):
        return True
    return False

def verificaEmpate(tabuleiro):
    for linha in tabuleiro:
        if '_' in linha:
            return False
    return True

# Função principal do jogo (não vamos aplicar cores nos símbolos armazenados)
def jogo(galo, sJ1, sJ2, espaco, jogador1, jogador2):
    for i in range(9):
        mostraTabuleiro(galo, 3, 3)
        # Alterna entre os jogadores
        simbolo = sJ1 if i % 2 == 0 else sJ2
        print("\nJogador", simbolo)
        # Validação da jogada: linha
        while True:
            linha = inputVazio("Linha 1..3: ")
            if linha not in ("1", "2", "3"):
                print("Coordenadas inválidas! Por favor, insira valores entre 1 e 3.")
                continue
            linha = int(linha)
            break
        # Validação da jogada: coluna
        while True:
            coluna = inputVazio("Coluna 1..3: ")
            if coluna not in ("1", "2", "3"):
                print("Coordenadas inválidas! Por favor, insira valores entre 1 e 3.")
                continue
            coluna = int(coluna)
            break
        print(espaco)
        if galo[linha-1][coluna-1] == '_':
            galo[linha-1][coluna-1] = simbolo
        else:
            print("\n------ Posição ocupada, escolha outra!!!\n")
            mostraTabuleiro(galo, 3, 3)
            print("\nJogador", simbolo)
            continue  # Permite repetir a jogada se a posição estiver ocupada

        # Verifica vencedor ou empate
        if verificaVencedor(galo, simbolo):
            mostraTabuleiro(galo, 3, 3)
            # Determina o vencedor com base no símbolo
            if simbolo == jogador1[1]:
                vencedor = jogador1[0]
            else:
                vencedor = jogador2[0]
            print(" -- Venceu o(a) " + vencedor + ": " + simbolo)
            return simbolo
        elif verificaEmpate(galo):
            mostraTabuleiro(galo, 3, 3)
            print(" -- Empate!")
            return "empate"
    return None

# --- Programa Principal ---

empates = 0
espaco = "\n" * 3
pResumo = "9 - Ver resumo\n10 - Limpar os dados"
PSair = "12 - Sair"
# NÃO vamos trocar os jogadores (removemos o swap)
jogador1, jogador2 = inicializaJogadores()

# Garantir que os símbolos estejam definidos corretamente
if jogador1[1] not in ("X", "O"):
    jogador1[1] = "X"
jogador2[1] = "O" if jogador1[1] == "X" else "X"

while True:
    opcao = int(input("Escolha uma opção: "))  # Simplificado para exemplificar
    # Programa principal
    galo = criaTabuleiro(3, 3, 0)
    galo = inicializaTabuleiro(galo, 3, 3, '_')
    
    if opcao == 1:
        # Os símbolos são armazenados puros (sem cores)
        simboloJ1 = jogador1[1]
        simboloJ2 = jogador2[1]
        
        while True:  # Jogar enquanto os jogadores desejarem
            galo = inicializaTabuleiro(galo, 3, 3, '_')
            resultado = jogo(galo, simboloJ1, simboloJ2, espaco, jogador1, jogador2)
            if resultado == simboloJ1:
                jogador1[3] += 1
            elif resultado == simboloJ2:
                jogador2[3] += 1
            elif resultado == "empate":
                empates += 1
            
            numeroDeJogos = jogador1[3] + jogador2[3] + empates
            continuar = inputVazio("Deseja jogar novamente (S/N): ").upper()
            if continuar == "N":
                print(espaco)
                print(jogador1[0], "têm", jogador1[3], "vitória(s),", (jogador1[3] / numeroDeJogos) * 100, "%")
                print(jogador2[0], "têm", jogador2[3], "vitória(s),", (jogador2[3] / numeroDeJogos) * 100, "%")
                print("Empates:", empates, ",", (empates / numeroDeJogos) * 100, "%")
                break
            else:
                print(espaco)
                
    elif opcao == 7:
        print(espaco)
        resumo(jogador1[0], jogador2[0], jogador1[3], jogador2[3], empates)
        
    elif opcao == 8:
        print(espaco)
        print("Os dados foram todos colocados com os valores padrões de início.")
        jogador1, jogador2 = inicializaJogadores()
        
    elif opcao == 9:
        print(espaco)
        print("A sair do jogo....")
        resumo(jogador1[0], jogador2[0], jogador1[3], jogador2[3], empates)
        break
    else:
        print("Opção inválida")
