# Códigos ANSI para cores:
PREDEFENIDO = ""
AMARELO    = "\033[1;33m"   
AZUL       = "\033[1;34m"      
BRANCO     = "\033[1;37m"    
CIANO      = "\033[0;36m"     
ROXO       = "\033[1;35m"      
VERDE      = "\033[1;32m"     
VERMELHO   = "\033[1;31m"  
END        = "\033[0m"  # Reseta a formatação

############# CONFIGURAÇÕES E MENUS
opcao      = 0
espaco     = "\n" * 5
pResumo    = "7 - Ver resumo\n8 - Limpar os dados"
PSair      = "9 - Sair"
PVoltar    = "9 - Voltar ao menu anterior"
update     = ""
inputCores = ("0 - PREDEFENIDO\n1 - AMARELO\n2 - AZUL\n3 - BRANCO\n"
              "4 - CIANO\n5 - ROXO\n6 - VERDE\n7 - VERMELHO\n"
              "Enumere a cor que deseja utilizar para os seus símbolos: ")

# Função para exibir o resumo dos jogos:
def resumo(nome1, nome2, vitorias1, vitorias2, empates):
    numeroDeJogos = vitorias1 + vitorias2 + empates
    print("\n--- Resumo de", numeroDeJogos, "Jogo(s) ---")
    if numeroDeJogos > 0:
        print(nome1, "têm", vitorias1, "vitória(s),", (vitorias1 / numeroDeJogos) * 100, "%")
        print(nome2, "têm", vitorias2, "vitória(s),", (vitorias2 / numeroDeJogos) * 100, "%")
        print("Empates:", empates, ",", (empates / numeroDeJogos) * 100, "%")
    else:
        print("Nenhuma partida foi concluída!")

# Funções de tabuleiro:
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

# Funções para verificação de vencedor e empate:
def verificaVencedor(tabuleiro, simbolo):
    # Verifica linhas e colunas:
    for i in range(3):
        if (tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == simbolo) or \
           (tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == simbolo):
            return True
    # Verifica diagonais:
    if (tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == simbolo) or \
       (tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == simbolo):
        return True
    return False

def verificaEmpate(tabuleiro):
    for linha in tabuleiro:
        if '_' in linha:
            return False
    return True

# Função que executa uma partida:
def jogo(galo, sJ1, sJ2, espaco):
    for i in range(9):
        mostraTabuleiro(galo, 3, 3)
        # Alterna entre os jogadores:
        if i % 2 == 0:
            simbolo = sJ1
        else:
            simbolo = sJ2

        print("\nJogador", simbolo)
        # Solicita a jogada:
        while True:
            try:
                linha = int(input("Linha 1..3: "))
                if linha not in (1, 2, 3):
                    print("Coordenadas inválidas! Insira valores entre 1 e 3.")
                    continue
                coluna = int(input("Coluna 1..3: "))
                if coluna not in (1, 2, 3):
                    print("Coordenadas inválidas! Insira valores entre 1 e 3.")
                    continue
            except ValueError:
                print("Entrada inválida! Digite um número.")
                continue
            print(espaco)
            if galo[linha - 1][coluna - 1] == '_':
                galo[linha - 1][coluna - 1] = simbolo
                break
            else:
                print("\n------ Posição ocupada, escolha outra! ------\n")
                mostraTabuleiro(galo, 3, 3)
                print("\nJogador", simbolo)
        if verificaVencedor(galo, simbolo):
            mostraTabuleiro(galo, 3, 3)
            print(" -- Venceu o jogador:", simbolo)
            return simbolo
        elif verificaEmpate(galo):
            mostraTabuleiro(galo, 3, 3)
            print(" -- Empate!")
            return "empate"
    return None

# Função para imprimir as estatísticas atuais (debug)
def debug_stats(jogadores, empates):
    print("\nDEBUG - Estatísticas:")
    print(jogadores[0][0], ":", jogadores[0][3])
    print(jogadores[1][0], ":", jogadores[1][3])
    print("Empates:", empates)
    print()

# Menu principal:
def menuPrincipal():
    print(espaco)
    print(".... JOGO DO GALO ....")
    print("1 - Jogar")
    print("2 - Personalizar")
    print("9 - Sair")
    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        opcao = 0
    return opcao

# Menu de personalização (submenu com opções de 1 a 5 e 7, 8 para resumo e limpar dados):
def menuPersonalizacao(jogador1, jogador2):
    global update
    print(espaco)
    print(update)
    print(".... => Personalizar ....")
    print("1 - Mudar nome do(a) " + jogador1[0])
    print("2 - Mudar cor do(a) " + jogador1[0])
    print("3 - Mudar nome do(a) " + jogador2[0])
    print("4 - Mudar cor do(a) " + jogador2[0])
    print("5 - Mudar Símbolo")
    print("7 - Ver resumo")
    print("8 - Limpar dados")
    print("9 - Voltar ao menu anterior")
    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        opcao = 0

    if opcao == 1:
        novoNome = input("Nome do primeiro jogador: ")
        while novoNome.strip() == "":
            novoNome = input("Nome do primeiro jogador: ")
        jogador1[0] = novoNome
        update = "Personalização efetuada: O nome do jogador 1 é " + jogador1[0]
    elif opcao == 2:
        inputCor_str = input(inputCores)
        while inputCor_str.strip() == "":
            inputCor_str = input(inputCores)
        inputCor = int(inputCor_str)
        if inputCor == 0:
            jogador1[2] = PREDEFENIDO; cor = "Predefenido"
        elif inputCor == 1:
            jogador1[2] = AMARELO;   cor = "Amarelo"
        elif inputCor == 2:
            jogador1[2] = AZUL;      cor = "Azul"
        elif inputCor == 3:
            jogador1[2] = BRANCO;    cor = "Branco"
        elif inputCor == 4:
            jogador1[2] = CIANO;     cor = "Ciano"
        elif inputCor == 5:
            jogador1[2] = ROXO;      cor = "Roxo"
        elif inputCor == 6:
            jogador1[2] = VERDE;     cor = "Verde"
        elif inputCor == 7:
            jogador1[2] = VERMELHO;  cor = "Vermelho"
        else:
            jogador1[2] = PREDEFENIDO; cor = "Predefenido"
        update = "Personalização efetuada: A cor do(a) " + jogador1[0] + " é " + cor
    elif opcao == 3:
        novoNome = input("Nome do segundo jogador: ")
        while novoNome.strip() == "":
            novoNome = input("Nome do segundo jogador: ")
        jogador2[0] = novoNome
        update = "Personalização efetuada: O nome do jogador 2 é " + jogador2[0]
    elif opcao == 4:
        inputCor_str = input(inputCores)
        while inputCor_str.strip() == "":
            inputCor_str = input(inputCores)
        inputCor = int(inputCor_str)
        if inputCor == 0:
            jogador2[2] = PREDEFENIDO; cor = "Predefenido"
        elif inputCor == 1:
            jogador2[2] = AMARELO;   cor = "Amarelo"
        elif inputCor == 2:
            jogador2[2] = AZUL;      cor = "Azul"
        elif inputCor == 3:
            jogador2[2] = BRANCO;    cor = "Branco"
        elif inputCor == 4:
            jogador2[2] = CIANO;     cor = "Ciano"
        elif inputCor == 5:
            jogador2[2] = ROXO;      cor = "Roxo"
        elif inputCor == 6:
            jogador2[2] = VERDE;     cor = "Verde"
        elif inputCor == 7:
            jogador2[2] = VERMELHO;  cor = "Vermelho"
        else:
            jogador2[2] = PREDEFENIDO; cor = "Predefenido"
        update = "Personalização efetuada: A cor do(a) " + jogador2[0] + " é " + cor
    elif opcao == 5:
        novoSimbolo = input("Qual símbolo o " + jogador1[0] + " quer utilizar (X ou O): ").upper()
        while novoSimbolo.strip() == "":
            novoSimbolo = input("Qual símbolo o " + jogador1[0] + " quer utilizar (X ou O): ").upper()
        jogador1[1] = novoSimbolo
        jogador2[1] = "O" if novoSimbolo == "X" else "X"
        update = ("Personalização efetuada: " + jogador1[0] + " está com o símbolo " +
                  jogador1[1] + " e " + jogador2[0] + " está com " + jogador2[1])
    elif opcao == 7:
        resumo(jogador1[0], jogador2[0], jogador1[3], jogador2[3], empates)
    elif opcao == 8:
        # Reset dos dados para os padrões
        jogador1[:] = ["Jogador 1", "X", AMARELO, 0]
        jogador2[:] = ["Jogador 2", "O", AZUL, 0]
        empates = 0
        update = "Dados foram reiniciados para os valores padrão."
    # Se opcao for 9, apenas volta ao menu principal
    return

# Configuração inicial dos jogadores:
jogador1 = ["Jogador 1", "X", AMARELO, 0]
jogador2 = ["Jogador 2", "O", AZUL, 0]
jogadores = [jogador1, jogador2]
ordem = [0, 1]  # jogadores[ordem[0]] inicia
empates = 0

# Verifica se os símbolos são válidos:
if jogador1[1] not in ("X", "O"):
    jogador1[1] = "X"
if jogador1[1] == "X":
    jogador2[1] = "O"
else:
    jogador2[1] = "X"

# Loop principal do jogo:
while True:
    opcao = menuPrincipal()
    if opcao == 2:
        menuPersonalizacao(jogadores[0], jogadores[1])
        print(update)
        continue
    elif opcao == 9:
        print(espaco)
        print("A sair do jogo....")
        resumo(jogadores[0][0], jogadores[1][0], jogadores[0][3], jogadores[1][3], empates)
        break
    elif opcao == 1:
        # Modo de jogo simples:
        primeiro = jogadores[ordem[0]]
        segundo  = jogadores[ordem[1]]
        simboloPrimeiro = primeiro[2] + primeiro[1] + END
        simboloSegundo  = segundo[2] + segundo[1] + END
        galo = criaTabuleiro(3, 3, 0)
        galo = inicializaTabuleiro(galo, 3, 3, '_')
        while True:
            galo = inicializaTabuleiro(galo, 3, 3, '_')
            resultado = jogo(galo, simboloPrimeiro, simboloSegundo, espaco)
            if resultado == simboloPrimeiro:
                jogadores[ordem[0]][3] += 1
                # Se o jogador que iniciou venceu, inverte a ordem (o perdedor passa a iniciar):
                ordem = [ordem[1], ordem[0]]
            elif resultado == simboloSegundo:
                jogadores[ordem[1]][3] += 1
                # Ordem permanece; o perdedor (primeiro) continua iniciando.
            elif resultado == "empate":
                empates += 1

            # Debug: exibe as estatísticas atuais
            debug_stats(jogadores, empates)
            
            continuar = input("Deseja jogar novamente (S/N): ").upper()
            if continuar == "N":
                break
            else:
                print(espaco)
                primeiro = jogadores[ordem[0]]
                segundo  = jogadores[ordem[1]]
                simboloPrimeiro = primeiro[2] + primeiro[1] + END
                simboloSegundo  = segundo[2] + segundo[1] + END
    else:
        print("Opção inválida!")
