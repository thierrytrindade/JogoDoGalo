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


#Funções e seus significados
#continue - serve para recomeçar um while
opcao = 0
espaco = "\n"*100




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

def menuJogo(vitorias1, vitorias2, empates,espaco):
    pResumo="7 - Ver resumo\n8 - Limpar os dados"
    temResumo = vitorias1 + vitorias2 + empates
    contaMenus = 0
    Rodadas = 0
    Verifica=0
    opcao=0
    print(espaco)
    """ if temResumo == 0:
        opcoesValidas = (1, 2, 9)
    else:
        opcoesValidas = (1, 2, 3, 4, 9) """
    while True:
        if contaMenus == 7 and temResumo > 0:
            opcao=7
            return opcao
        if contaMenus == 8 and temResumo > 0:
            opcao=8
            return opcao
        if Rodadas == -1:
            contaMenus=0
            opcao=9
            return opcao
        
        if contaMenus == 0 and Rodadas==0 and Verifica==0:
            if temResumo == 0:
                opcoesValidas = (1, 2, 9)
            else:
                opcoesValidas = (1, 2, 7, 8, 9)
            print(".... JOGO DO GALO ....")
            print("1 - Jogar")
            print("2 - Personalizar")
            if temResumo > 0: # permite ter um menu dinamico fazendo com que o menu mude automaticamente caso tenha havido ou nao partida concluida
                print(pResumo)
            print("9 - Sair")


        if contaMenus==1 and Rodadas==1:
            contaMenus=0
            if temResumo == 0:
                opcoesValidas = (1, 2, 3, 4, 9)
            else:
                opcoesValidas = (1, 2, 3, 4, 7, 8, 9)
            print(".... JOGO DO GALO ....")
            print("1 - Partida simples/indefenida (VER ERROS ORTHOGRAFICOS !)\n2 - Maior de 3\n3 - Maior de 5\n4 - Parsonalizar o número de jogos")
            if temResumo > 0: # permite ter um menu dinamico fazendo com que o menu mude automaticamente caso tenha havido ou nao partida concluida
                print(pResumo)
            print("9 - Voltar ao menu anterior")
        if contaMenus==2 and Rodadas==1:
            contaMenus=0
            if temResumo == 0:
                opcoesValidas = (1, 2, 3, 4, 5, 9)
            else:
                opcoesValidas = (1, 2, 3, 4, 5, 7, 8, 9)        
            print("1 - Mudar nome jogador 1")
            print("2 - Mudar cor jogador 1")
            print("3 - Mudar nome jogador 2")
            print("4 - Mudar cor jogador 2")
            print("5 - Mudar simbolo ")
            if temResumo > 0: # permite ter um menu dinamico fazendo com que o menu mude automaticamente caso tenha havido ou nao partida concluida
                print(pResumo)
            print("9 - Voltar ao menu anterior")
            Verifica=1
        if Rodadas==3:
            if Verifica==0:
                if contaMenus==1:
                    opção=1
                    return opcao
                if contaMenus==2:
                    opção=2
                    return opcao
                if contaMenus==3:
                    opção=3
                    return opcao
            if Verifica==1:
                Verifica=0
                if contaMenus==1:
                    opção=4
                    return opcao
                if contaMenus==2:
                    opção=5
                    return opcao
                if contaMenus==3:
                    opção=6#Salta opção 7 e 8, pois ja fasso return atras
                    return opcao
                if contaMenus==4:
                    opção=10
                    return opcao
                if contaMenus==5:
                    opção=11
                    return opcao



        contaMenus = int(input("Escolha uma opção: "))
        if contaMenus== 9:
            Rodadas-=1
        elif contaMenus== 9:
            Rodadas-=1
        elif contaMenus in opcoesValidas and contaMenus!= 9:
            Rodadas+=1
        elif contaMenus not in opcoesValidas:
            print(espaco)
            print("Entrada inválida! Por favor, insira um número válido.")


        
# menuJogoBase
## 
# menuJogoJversosJ
# menuJogoJversosC




def menuJogoBase(vitorias1, vitorias2, empates,espaco):
    temResumo = vitorias1 + vitorias2 + empates
    print(espaco)
    if temResumo == 0:
        opcoesValidas = (1, 2, 9)
    else:
        opcoesValidas = (1, 2, 3, 4, 9)
    while True:
        
        print(".... JOGO DO GALO ....")
        print("1 - Jogar contra outro jogador")
        print("2 - Jogar contra o computador")
        if temResumo > 0: # permite ter um menu dinamico fazendo com que o menu mude automaticamente caso tenha havido ou nao partida concluida
            print("7 - Ver resumo")
            print("8 - Limpar os dados")
        print("9 - Voltar ao menu anterior")

        opcao = int(input("Escolha uma opção: "))

        if opcao not in opcoesValidas:
            print(espaco)
            print("Entrada inválida! Por favor, insira um número válido.")
            """continue"""
        else : 
            return opcao



def menuJogoJversusJ(vitorias1, vitorias2, empates,espaco):
    temResumo = vitorias1 + vitorias2 + empates
    print(espaco)
    if temResumo == 0:
        opcoesValidas = (1, 2, 9)
    else:
        opcoesValidas = (1, 2, 3, 4, 9)
    while True:
        
        print(".... JOGO DO GALO ....")
        print("1 - Jogar")
        print("2 - Personalizar")
        if temResumo > 0: # permite ter um menu dinamico fazendo com que o menu mude automaticamente caso tenha havido ou nao partida concluida
            print("3 - Ver resumo")
            print("4 - Limpar os dados")
        print("9 - Voltar ao menu anterior")


        opcao = int(input("Escolha uma opção: "))

        if opcao not in opcoesValidas:
            print(espaco)
            print("Entrada inválida! Por favor, insira um número válido.")
            """continue"""
        else : 
            return opcao



def menuJogoJversusC(vitorias1, vitorias2, empates,espaco):
    temResumo = vitorias1 + vitorias2 + empates
    print(espaco)
    if temResumo == 0:
        opcoesValidas = (1, 2, 9)
    else:
        opcoesValidas = (1, 2, 3, 4, 9)
    while True:
        
        print(".... JOGO DO GALO ....")
        print("1 - Jogar")
        print("2 - Personalizar")
        if temResumo > 0: # permite ter um menu dinamico fazendo com que o menu mude automaticamente caso tenha havido ou nao partida concluida
            print("3 - Ver resumo")
            print("4 - Limpar os dados")
        print("9 - Voltar ao menu anterior")


        opcao = int(input("Escolha uma opção: "))

        if opcao not in opcoesValidas:
            print(espaco)
            print("Entrada inválida! Por favor, insira um número válido.")
            """continue"""
        else : 
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

def jogo(galo, sJ1, sJ2, espaco):
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
            print(espaco)# Turna o jogo mais "limpo", mostrando só o tabuleiro 
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

# Definir variáveis de estatísticas fora do loop principal
jogador1 = ["Jogador 1", "X", "cor", 0]

jogador2 = ["Jogador 2", "O", "cor", 0]
empates = 0

# A RETIFICAR DEPOIS !
if jogador1[1] != "X" and jogador1[1] != "O":
    jogador1[1] = "X"
    
if jogador1[1] == "X":
    jogador2[1] = "O"
else:
    jogador2[1]= "X"

while True:
    opcao = menuJogo(jogador1[3], jogador2[3], empates, espaco)

    # Programa principal
    galo = criaTabuleiro(3, 3, 0)
    galo = inicializaTabuleiro(galo, 3, 3, ' ')


    if opcao == 1:
        

        simboloJ1 = jogador1[1]
        simboloJ2 = jogador2[1]
        # ATÉ AQUI !


        while True: #Jogar enquanto os jogadores o entenderem  
            galo = inicializaTabuleiro(galo, 3, 3, '_')  # Limpa o tabuleiro

            # Realiza uma partida
            resultado = jogo(galo, simboloJ1, simboloJ2)
            # Atualiza estatísticas
            if resultado == simboloJ1:
                jogador1[3] += 1
            elif resultado == simboloJ2:
                jogador2[3] += 1
            elif resultado == "empate":
                empates += 1
            # Pergunta se deseja continuar jogando
            continuar = input("Deseja jogar novamente (S/N): ").upper()
            if continuar == "N":
                break
            else: 
                print(espaco)# Turna o jogo mais "limpo", mostrando só o tabuleiro
            # Opcional: alterna os símbolos para a próxima partida
            simboloJ1, simboloJ2 = simboloJ2, simboloJ1



    elif opcao == 2:
            # Dados dos jogadores: [nome, símbolo, vitórias]
        jogador1[0]=input("Nome do primeiro jogador: ")
        jogador1[1]=input("Qual símbolo que quer utilizar (X ou O): ").upper()
        jogador1[3]=0
        # RETIFICAR A VALIDACAO DO SIMBOLO É NECESSARIA ISTO É APENAS TEMPORARIO PARA REALIZAR A VERIFICACAO DO RESUMO ESTATISTICO

        escolha = int(input("\t1---> para jogar com outra pessoa\nOpção: "))
        # escolha = int(input("\t1---> para jogar com outra pessoa\n\t2---> para jogar com o computador\nOpção: "))
        if escolha == 1:
            
            jogador2[0] = input("Nome do segundo jogador: ")
            jogador2[1] = "O" if jogador1[1] == "X" else "X"
            jogador2[3] = 0

        else:
            # Define o símbolo automaticamente para o computador
            
            jogador2[0] = "Computador"
            jogador2[1] = "O" if jogador1[1] == "X" else "X"
            jogador2[3] = 0
        
        simboloJ1 = jogador1[1]
        simboloJ2 = jogador2[1]
        
    elif opcao == 7:

        print(espaco)# Turna o jogo mais "limpo"
        resumo(jogador1[0], jogador2[0], jogador1[3], jogador2[3], empates)

        
    elif opcao == 8:

        print(espaco)# Turna o jogo mais "limpo"
        print("Os dados foram todos colocados com os valores padroes de inicio.")
        jogador1[0]="Jogador 1"
        jogador1[1]="X"
        jogador1[3]=0
        jogador2[0] = "Jogador 2"
        jogador2[1] = "O" if jogador1[1] == "X" else "X"
        jogador2[3] = 0


    elif opcao == 9:
        print(espaco)# Turna o jogo mais "limpo"
        print("A sair do jogo....")

        resumo(jogador1[0], jogador2[0], jogador1[3], jogador2[3], empates)


        break


    else:
        print("Opção inválida")
