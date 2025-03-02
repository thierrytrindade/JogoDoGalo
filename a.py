############# ERROS
# - Se o usuário inserir um número fora de 1 a 3, deve solicitar a entrada novamente.
# - ADICIONAR A FUNÇÃO DE NÃO PERMITIR NOME VAZIO PARA O JOGADOR.
# - O JOGO SÓ DEVE PERMITIR 9 JOGADAS.

# Jogo do Galo com vetor unidimensional (9 elementos)
# Estrutura de dados: 
#   - Tabuleiro: vetor com 9 posições (índices 0 a 8)
#   - Jogadores: cada um é um vetor com [nome, símbolo, vitórias]

def criaTabuleiro(valor):
    """Cria um vetor com 9 posições, inicializado com 'valor'."""
    return [valor] * 9

def inicializaTabuleiro(tab, valor):
    """Inicializa o tabuleiro (vetor) atribuindo 'valor' a todas as posições."""
    for i in range(9):
        tab[i] = valor
    return tab

def mostraTabuleiro(tab):
    """Mostra o tabuleiro em formato 3x3 usando o vetor unidimensional."""
    for i in range(3):
        linha = " | ".join(tab[i*3:(i+1)*3])
        print(" " + linha)
        if i < 2:
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

def verificaVencedor(tab, simbolo):
    """Verifica se o 'simbolo' venceu verificando linhas, colunas e diagonais."""
    # Linhas
    for i in range(3):
        if tab[i*3] == simbolo and tab[i*3+1] == simbolo and tab[i*3+2] == simbolo:
            return True
    # Colunas
    for i in range(3):
        if tab[i] == simbolo and tab[i+3] == simbolo and tab[i+6] == simbolo:
            return True
    # Diagonais
    if tab[0] == simbolo and tab[4] == simbolo and tab[8] == simbolo:
        return True
    if tab[2] == simbolo and tab[4] == simbolo and tab[6] == simbolo:
        return True
    return False

def verificaEmpate(tab):
    """Retorna True se o tabuleiro estiver cheio (empate), ou False caso contrário."""
    return ' ' not in tab

def obterEntradaNumero(mensagem):
    """Lê um número inteiro entre 1 e 3, validando a entrada."""
    while True:
        try:
            num = int(input(mensagem))
            if 1 <= num <= 3:
                return num
            else:
                print("Número inválido! Insira um valor entre 1 e 3.")
        except ValueError:
            print("Entrada inválida! Por favor, insira um número.")

def obterNome(mensagem):
    """Obtém um nome não vazio para o jogador."""
    while True:
        nome = input(mensagem).strip()
        if nome != "":
            return nome
        else:
            print("Nome não pode ser vazio. Tente novamente.")

def jogo(tabuleiro, sJ1, sJ2):
    """Realiza uma partida do jogo, limitando a 9 jogadas e validando cada movimento."""
    for i in range(9):
        mostraTabuleiro(tabuleiro)
        # Alterna entre os jogadores
        if i % 2 == 0:
            simbolo = sJ1
        else:
            simbolo = sJ2
        # Validação da jogada
        while True:
            print(f"\nJogador {simbolo}")
            linha = obterEntradaNumero("Linha (1 a 3): ")
            coluna = obterEntradaNumero("Coluna (1 a 3): ")
            posicao = (linha - 1) * 3 + (coluna - 1)
            # Verifica se a posição está livre
            if tabuleiro[posicao] == ' ':
                tabuleiro[posicao] = simbolo
                break
            else:
                print("\n------ Posição ocupada, escolha outra!!!\n")
        # Verifica se houve vencedor
        if verificaVencedor(tabuleiro, simbolo):
            mostraTabuleiro(tabuleiro)
            print(" -- Venceu o jogador:", simbolo)
            return simbolo
        elif verificaEmpate(tabuleiro):
            mostraTabuleiro(tabuleiro)
            print(" -- Empate!")
            return "empate"
    return None

# Programa principal
galo = criaTabuleiro(' ')

# Definir os símbolos dos jogadores
simboloJ1 = 'X'
simboloJ2 = 'O'

# Obter dados dos jogadores garantindo que o nome não seja vazio
Jogador1 = [obterNome("Nome do primeiro jogador: "), input("Qual símbolo quer utilizar (X ou O): ").upper(), 0]

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
            galo = inicializaTabuleiro(galo, ' ')
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