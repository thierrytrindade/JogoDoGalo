############# ERROS
# - Se o usuário inserir um número fora de 1 a 3, deve solicitar a entrada novamente.
# - ADICIONAR A FUNÇÃO DE NÃO PERMITIR NOME VAZIO PARA O JOGADOR.
# - O JOGO SÓ DEVE PERMITIR 9 JOGADAS.

# Jogo do Galo
# Rotinas
"""
Estrutura de dados:
- Matriz 3x3 (vetor de 9 elementos organizados em 3 linhas e 3 colunas)
- Contador de vitórias por jogador e número de empates

Rotinas:
- Criar a matriz/tabuleiro
- Inicializar o tabuleiro de jogo
- Mostrar o tabuleiro (com formatação bonita)
- Mostrar menu do jogo
- Ler uma jogada e preencher o tabuleiro
- Verificar se após a jogada alguém ganhou
- Atualizar a pontuação do jogo
- Questionar se querem jogar novamente (novo jogo)
"""

def criaTabuleiro(l, c, v):
    m = []
    for i in range(l):
        linha = []
        for j in range(c):
            linha += [v]
        m += [linha]
    return m

def inicializaTabuleiro(m, l, c, valor):
    for i in range(l):
        for j in range(c):
            m[i][j] = valor
    return m

def mostraTabuleiro(m, l, c):
    # Mostra o tabuleiro em formato 3x3.
    for i in range(l):
        # Junta os elementos da linha com " | " como separador
        linha = " | ".join(m[i])
        print(" " + linha)
        if i < l - 1:
            print("---+---+---")

def menuJogo():
    print(".... JOGO DO GALO ....")
    print("1 - Jogar")
    print("2 - Sair")
    try:
        op = int(input("Escolha uma opção: "))
    except ValueError:
        op = 0
    return op

def verificaVencedor(tabuleiro, simbolo):
    # Verifica linhas e colunas
    for i in range(3):
        if (tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == simbolo) or \
           (tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == simbolo):
            return True
    # Verifica diagonais
    if (tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == simbolo) or \
       (tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == simbolo):
        return True
    return False

def verificaEmpate(tabuleiro):
    # Se não houver mais espaços vazios (' '), é empate.
    for linha in tabuleiro:
        if ' ' in linha:
            return False
    return True

def obterNome(mensagem):
    """Obtém um nome não vazio para o jogador."""
    while True:
        nome = input(mensagem).strip()
        if nome != "":
            return nome
        else:
            print("Nome não pode ser vazio. Tente novamente.")

def jogo(galo, sJ1, sJ2):
    for i in range(9):
        mostraTabuleiro(galo, 3, 3)
        # Alterna entre os jogadores
        if i % 2 == 0:
            simbolo = sJ1
        else:
            simbolo = sJ2
        # Validação da jogada
        while True:
            print("\nJogador", simbolo)
            try:
                linha = int(input("Linha 1..3: "))
                coluna = int(input("Coluna 1..3: "))
            except ValueError:
                print("Por favor, insira números válidos.")
                continue
            # Verifica se as coordenadas estão dentro do intervalo permitido
            if linha < 1 or linha > 3 or coluna < 1 or coluna > 3:
                print("Coordenadas inválidas! Por favor insira valores entre 1 e 3.")
                continue
            # Verifica se a posição está livre
            if galo[linha-1][coluna-1] == ' ':
                galo[linha-1][coluna-1] = simbolo
                break
            else:
                print("\n------ Posição ocupada, escolha outra!!!\n")
        # Verifica se houve vencedor
        if verificaVencedor(galo, simbolo):
            mostraTabuleiro(galo, 3, 3)
            print(" -- Venceu o jogador:", simbolo)
            return simbolo
        elif verificaEmpate(galo):
            mostraTabuleiro(galo, 3, 3)
            print(" -- Empate!")
            return "empate"
    return None

# Programa principal
galo = criaTabuleiro(3, 3, 0)
galo = inicializaTabuleiro(galo, 3, 3, ' ')

# Definir os símbolos dos jogadores
simboloJ1 = 'X'
simboloJ2 = 'O'

# Dados dos jogadores: [nome, símbolo, vitórias]
Jogador1 = [obterNome("Nome do primeiro jogador: "), input("Qual símbolo que quer utilizar (X ou O): ").upper(), 0]
escolha = int(input("\t1---> para jogar com outra pessoa\n\t2---> para jogar com o computador\nOpção: "))
if escolha == 1:
    Jogador2 = [obterNome("Nome do segundo jogador: "), "O" if Jogador1[1] == "X" else "X", 0]
else:
    # Define o símbolo automaticamente para o computador
    Jogador2 = ["Computador", "O" if Jogador1[1] == "X" else "X", 0]

simboloJ1 = Jogador1[1]
simboloJ2 = Jogador2[1]

empates = 0

while True:
    op = menuJogo()
    if op == 1:
        while True:
            # Limpa o tabuleiro para nova partida
            galo = inicializaTabuleiro(galo, 3, 3, ' ')

            # Realiza uma partida
            resultado = jogo(galo, simboloJ1, simboloJ2)
            # Atualiza estatísticas
            if resultado == simboloJ1:
                Jogador1[2] += 1
            elif resultado == simboloJ2:
                Jogador2[2] += 1
            elif resultado == "empate":
                empates += 1

            continuar = input("Deseja jogar novamente (S/N): ").upper()
            if continuar == "N":
                break

            # Opcional: alterna os símbolos para a próxima partida
            simboloJ1, simboloJ2 = simboloJ2, simboloJ1

    elif op == 2:
        print("A sair do jogo....")
        print("\n--- Resumo do Jogo ---")
        print("Jogador 1 (", Jogador1[0], "): ", Jogador1[2], " vitória(s)", sep="")
        print("Jogador 2 (", Jogador2[0], "): ", Jogador2[2], " vitória(s)", sep="")
        print("Empates:", empates)
        break
    else:
        print("Opção inválida")