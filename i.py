""" 
Enumere a cor que deseja utilizar para os seus simbolos

0	 -	PREDEFENIDO
1	 - 	AMARELO = "\033[1;33m"
2	 - 	AZUL = "\033[1;34m"
3	 - 	BRANCO = "\033[1;37m"
4	 - 	CASTANHO = "\033[0;33m"
5	 - 	CIANO = "\033[0;36m"
6	 - 	CINZENTO = "\033[1;30m"
7	 - 	PRETO = "\033[0;30m"
8	 - 	ROXO = "\033[1;35m"
9	 - 	VERDE = "\033[1;32m"
10	 - 	VERMELHO = "\033[1;31m"
END = "\033[0m"  #Anula a formatação anterior
 """
PREDEFENIDO = 0
AMARELO = "\033[1;33m"
AZUL = "\033[1;34m"
BRANCO = "\033[1;37m"
CASTANHO = "\033[0;33m"
CIANO = "\033[0;36m"
CINZENTO = "\033[1;30m"
PRETO = "\033[0;30m"
ROXO = "\033[1;35m"
VERDE = "\033[1;32m"
VERMELHO = "\033[1;31m"
END = "\033[0m"  #Anula a formatação anterior

############# ERROS
# meter um numero diferente de 1-3 e andar para a frente sem aparecer erro por exemplo meti 23 em vez de 2 e depois 3 na alinea a seguir e avançou
# ADICIONAR A FUNCAO DE NAO DEFINIR O NOME DO JOGADOR
# O JOGO SO DEVE PERMITIR 9 JOGADAS.

# Jogo do Galo
# Rotinas
"""
Estrutura de dados
Matriz 3x3 | vetor 9 elementos
num_vitorias por jogador, num_empates

criar a matriz/vetor 
inicializar a matriz (tabuleiro de jogo)
mostrar a matriz (tabuleiro de jogo)
mostrar menu do jogo
ler uma jogada e preencher o tabuleiro
verificar se após jogada alguém ganhou
atualizar a pontuação do jogo
questionar se querem voltar a jogar (novo jogo)
"""



def resumo(nome1,nome2,vitorias1,vitorias2,empate):
    numeroDeJogos = 0
    print("\n--- Resumo do(s)", numeroDeJogos," Jogo(s) ---")
    numeroDeJogos=vitorias1+vitorias2+empates
    if nome1!="":
        print("Jogador 1 (", nome1, ") :", vitorias1, " vitória(s),",vitorias1/numeroDeJogos,"%")    
    else:
        print("Jogador 1 :", vitorias1, " vitória(s),",vitorias1/numeroDeJogos,"%")
    if nome2!="":
        print("Jogador 2 (", nome2, ") :", vitorias2, " vitória(s),",vitorias2/numeroDeJogos,"%")
    else:
        print("Jogador 2 :", vitorias2, " vitória(s),",vitorias2/numeroDeJogos,"%")
    print("Empates:", empate)

def criaTabuleiro(linha, coluna, valor):
    tabuleiro = [] # tabuleiro é igual a matriz
    for i in range(linha):
        linhai = []
        for j in range(coluna):
            linhai += [valor]
        tabuleiro += [linhai]
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

def menuJogo():
    print(".... JOGO DO GALO ....")
    print("1 - Jogar")
    print("2 - Personalizar")
    print("3 - Sair")
    opcao = int(input("Escolha uma opção: "))
    return opcao

def verificaVencedor(tabuleiro, simbolo):
    # Verifica linhas e colunas
    for i in range(3):
        if (tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == simbolo) or (tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == simbolo):
            return True
    # Verifica diagonais
    if (tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == simbolo) or (tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == simbolo):
        return True
    return False

def verificaEmpate(tabuleiro):
    for linha in tabuleiro:
        if '_' in linha:
            return False  # Ainda há jogadas disponíveis
    return True  # Tabuleiro cheio, é empate

def jogo(galo, sJ1, sJ2):
    for i in range(9):
        mostraTabuleiro(galo, 3, 3)
        # Alterna entre os jogadores
        if i % 2 == 0:
            simbolo = sJ1
        else:
            simbolo = sJ2

        # Validação da jogada
        print("\nJogador", simbolo)
        while True:        
            while True :
                linha = int(input("Linha 1..3: "))
                # Verifica se as coordenadas estão dentro do intervalo permitido
                if linha not in(1,2,3): 
                    print("Coordenadas inválidas! Por favor insira valores entre 1 a 3.")
                    continue
                else:
                    break
            while True :
                coluna = int(input("Coluna 1..3: "))
                # Verifica se as coordenadas estão dentro do intervalo permitido
                if coluna not in (1,2,3):
                    print("Coordenadas inválidas! Por favor insira valores entre 1 a 3.")
                    continue
                else:
                    break
            print("\n"*130)# Turna o jogo mais "limpo", mostrando só o tabuleiro 
            if galo[linha-1][coluna-1] == '_':
                galo[linha-1][coluna-1] = simbolo
                break     
            else:
                print("\n------ Posição ocupada, escolha outra!!!\n") 
                mostraTabuleiro(galo, 3, 3)
                print("\nJogador", simbolo)#repito a chamada do jugador, pois como faço 130 linhas para continuar a saber qual o jogador a jogar
                
        # Verifica se houve vencedor
        if verificaVencedor(galo, simbolo):
            mostraTabuleiro(galo, 3, 3)
            print(" -- Venceu o jogador:", simbolo)
            return simbolo
        elif verificaEmpate(galo):
            mostraTabuleiro(galo, 3, 3)
            print(" -- Empate!")
            return "empate"
    return None #returna nada para prevenir erros(é uma proteção do código)
jogador1 = ["", "X", "", 0]
jogador2 = ["", "O", "", 0]
empates = 0


while True:
    opcao = menuJogo()

    # Programa principal
    galo = criaTabuleiro(3, 3, 0)
    galo = inicializaTabuleiro(galo, 3, 3, ' ')

    """ jogador1 = ["", "X", "", 0]
    jogador2 = ["", "O", "", 0] """

    # Dados dos jogadores: [nome, símbolo, vitórias]
    jogador1 = [input("Nome do primeiro jogador: "), input("Qual símbolo que quer utilizar (X ou O): ").upper(), 0]
    escolha = int(input("\t1---> para jogar com outra pessoa\nOpção: "))
    # escolha = int(input("\t1---> para jogar com outra pessoa\n\t2---> para jogar com o computador\nOpção: "))
    if escolha == 1:
        jogador2 = [input("Nome do segundo jogador: "), "O" if jogador1[1] == "X" else "X", 0]
    else:
        # Define o símbolo automaticamente para o computador
        jogador2 = ["Computador", "O" if jogador1[1] == "X" else "X", 0]
    simboloJ1 = jogador1[1]
    simboloJ2 = jogador2[1]
    

    


    if opcao == 1:
        while True: #Jogar enquanto os jogadores o entenderem  
            galo = inicializaTabuleiro(galo, 3, 3, '_')  # Limpa o tabuleiro

            # Realiza uma partida
            resultado = jogo(galo, simboloJ1, simboloJ2)
            # Atualiza estatísticas
            if resultado == simboloJ1:
                jogador1[2] += 1
            elif resultado == simboloJ2:
                jogador2[2] += 1
            elif resultado == "empate":
                empates += 1
            # Pergunta se deseja continuar jogando
            continuar = input("Deseja jogar novamente (S/N): ").upper()
            if continuar == "N":
                break
            else: 
                print("\n"*130)# Turna o jogo mais "limpo", mostrando só o tabuleiro
            # Opcional: alterna os símbolos para a próxima partida
            simboloJ1, simboloJ2 = simboloJ2, simboloJ1
        """
    elif opção ==2:
            # Dados dos jogadores: [nome, símbolo, vitórias]
        jogador1 = [input("Nome do primeiro jogador: "), input("Qual símbolo que quer utilizar (X ou O): ").upper(), 0]
        escolha = int(input("\t1---> para jogar com outra pessoa\nOpção: "))
        # escolha = int(input("\t1---> para jogar com outra pessoa\n\t2---> para jogar com o computador\nOpção: "))
        if escolha == 1:
            jogador2 = [input("Nome do segundo jogador: "), "O" if jogador1[1] == "X" else "X", 0]
        else:
            # Define o símbolo automaticamente para o computador
            jogador2 = ["Computador", "O" if jogador1[1] == "X" else "X", 0]
        simboloJ1 = jogador1[1]
        simboloJ2 = jogador2[1]   

        """
    elif opcao == 3:
        print("A sair do jogo....")

        resumo(jogador1[0], jogador2[0], jogador1[2], jogador2[2], empates)

        """ print("\n--- Resumo do Jogo ---")
        if jogador1[0]!="":
            print("Jogador 1 (", jogador1[0], ") :", jogador1[2], " vitória(s)")    
        else:
            print("Jogador 1 :", jogador1[2], " vitória(s)")
        if jogador2[0]!="":
            print("Jogador 2 (", jogador2[0], ") :", jogador2[2], " vitória(s)")
        else:
            print("Jogador 2 :", jogador2[2], " vitória(s)") 
            
        print("Empates:", empates)"""
        break


    else:
        print("Opção inválida")