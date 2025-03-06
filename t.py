
PREDEFENIDO = ""
AMARELO = "\033[1;33m"   
AZUL = "\033[1;34m"      
BRANCO = "\033[1;37m"    
CIANO = "\033[0;36m"     
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


def inputVazio(mensagem):
    while True:
        valor = input(mensagem)
        if valor == "":
            print("Você não digitou nada! Por favor, insira um valor válido.")
        else:
            return valor

        
""" def inputValidar(mensagem, opcoesValidas, espaco):
    while True:
        valor = input(mensagem)
        if valor in opcoesValidas:
            print(espaco)
            return valor
        print("Entrada inválida! Por favor, insira um valor válido.") """

def inicializaJogadores():
    return [
        ["Jogador 1", "X", PREDEFENIDO, 0],
        ["Jogador 2", "O", PREDEFENIDO, 0]
    ]


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

        







def menuJogo(vitorias1, vitorias2, empates,espaco,pResumo,PSair):
    temResumo = vitorias1 + vitorias2 + empates
    print(espaco)
    if temResumo == 0:
        opcoesValidas = ("1", "2", "9")
    else:
        opcoesValidas = ("1", "2", "7", "8", "9")
    while True:
        
        print(".... JOGO DO GALO ....")
        print("1 - Jogar")
        print("2 - Personalizar")
        if temResumo > 0: # permite ter um menu dinamico fazendo com que o menu mude automaticamente caso tenha havido ou nao partida concluida
            print(pResumo)
        print(PSair)

        opcao = input("Escolha uma opção: ")

        if opcao not in opcoesValidas:
            print(espaco)
            print("Entrada inválida! Por favor, insira um número válido.")
            """ continue """
        else :
            opcao=int(opcao) #em vez de meter no input meto aqui, assim consigo fazer a verificação de se o valor introduzido no codigo é simplesmente um enter ou nao, pois metendo in(input(...)) caso que a pessoa simplesmente fizesse enter dava logo erro fechando o programa e a ideia é podermos verificar e permitir ao utilizador de retificar os seus erros sem ter que ter que andar sempre a abrir o programa de novo apos um erro e assim nao tendo que voltar a fazer tudo o que ja tinha feito antes e que foi perdido pelo programa se fechar
            return opcao








def menuJogo(vitorias1, vitorias2, empates,espaco,menuTemporario, update, jogador1, jogador2):
    pResumo ="7 - Ver resumo\n8 - Limpar os dados"
    pSair = "9 - Sair"
    pVoltar ="9 - Voltar ao menu anterior"
    
    temResumo = vitorias1 + vitorias2 + empates
    print(espaco)

    while True:
        if menuTemporario==1:
            if temResumo == 0:
                opcoesValidas = ("1", "2", "9")
            else:
                opcoesValidas = ("1", "2", "9") + ("7", "8")
                
            print(espaco)
            print(".... JOGO DO GALO ....")
            print("1 - Jogar")
            print("2 - Personalizar")
            if temResumo > 0: # permite ter um menu dinamico fazendo com que o menu mude automaticamente caso tenha havido ou nao partida concluida
                print(pResumo)
            print(pSair)

        if menuTemporario==2:
            if temResumo == 0:
                opcoesValidas = ("1", "2", "3", "4", "9")
            else:
                opcoesValidas = ("1", "2", "3", "4", "9") + ("7", "8")
                
            print(espaco)
            print(".... => Jogar ....")
            print("1 - Partida simples/indefenida (VER ERROS ORTHOGRAFICOS !)\n2 - Maior de 3\n3 - Maior de 5\n Parsonalizar o número de jogos")
            if temResumo > 0: # permite ter um menu dinamico fazendo com que o menu mude automaticamente caso tenha havido ou nao partida concluida
                print(pResumo)
            print(pVoltar)
            
        if menuTemporario==3:
            if temResumo == 0:
                opcoesValidas = ("1", "2", "3", "4", "5", "9")
            else:
                opcoesValidas = ("1", "2", "3", "4", "5", "9") + ("7", "8")
                
            print(espaco)
            print(update)
            print(".... => Personalizar ....")
            print("1 - Mudar nome do(a) " + jogador1)
            print("2 - Mudar cor do(a) " + jogador1)
            print("3 - Mudar nome do(a) " + jogador2)
            print("4 - Mudar cor do(a) " + jogador2)
            print("5 - Mudar Simbolo")
            if temResumo > 0: # permite ter um menu dinamico fazendo com que o menu mude automaticamente caso tenha havido ou nao partida concluida
                print(pResumo)
            print(pVoltar)

        
        opcao = inputVazio("Escolha uma opção: ")
        """ opcao = input("Escolha uma opção: ")
        while opcao == "":
            print("Você não digitou nada! Por favor, insira um nome válido.")
            opcao = input("Escolha uma opção: ") """

        if opcao not in opcoesValidas:
            print(espaco)
            print("Entrada inválida! Por favor, insira um número válido.")
        else : 

            if opcao == "7" or opcao == "8" : opcao=int(opcao); return opcao

            elif opcao == "9" and menuTemporario !=1 : menuTemporario = 1

            elif opcao == "9" and menuTemporario ==1 : opcao=int(opcao); return opcao

            elif menuTemporario == 1 and opcao == "1" : menuTemporario = 2
            
            elif menuTemporario == 1 and opcao == "2" : menuTemporario = 3

            #elif opcao == 9 and menuTemporario == 2 : menuTemporario = 1
            

            elif menuTemporario == 2 and opcao == "1" : opcao=int(opcao); return opcao

            elif menuTemporario == 2 and opcao == "2" : opcao=int(opcao); return opcao

            elif menuTemporario == 2 and opcao == "3" : opcao=int(opcao); return opcao

            elif menuTemporario == 2 and opcao == "4" : opcao=int(opcao); return opcao
            

            elif menuTemporario == 3 and opcao == "1" : opcao="5"; opcao=int(opcao); return opcao

            elif menuTemporario == 3 and opcao == "2" : opcao="6"; opcao=int(opcao); return opcao

            elif menuTemporario == 3 and opcao == "3" : opcao="10"; opcao=int(opcao); return opcao

            elif menuTemporario == 3 and opcao == "4" : opcao="11"; opcao=int(opcao); return opcao

            elif menuTemporario == 3 and opcao == "5" : opcao="12"; opcao=int(opcao); return opcao
            
            #elif menuTemporario == 3 and opcao == 9 : menuTemporario = 1



            
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

def jogo(galo, sJ1, sJ2, espaco, jogador1, jogador2):##########################################################################################################################################
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

                
                linha = inputVazio("Linha 1..3: ")
                """ linha = input("Linha 1..3: ")
                if linha == "": # serve para prevenir que o utilizador nao entre um valor vazio
                    print("Você não digitou nada! Por favor, insira um valor válido.")
                    continue """
                if linha != "1" and linha != "2" and linha != "3": # serve para prevenir que o utilizador nao entre um valor nao autorizado
                    print("Coordenadas inválidas! Por favor, insira valores entre 1 e 3.")
                    continue
                linha = int(linha) # serve para converter de string para int, visto que se eu tivesse int(input) nao deixava sequer prevenir o primeiro passo de ver se o campo é vazio e o jogo fechava logo de uma vez
                break

            while True :
                coluna = inputVazio("Coluna 1..3: ")
                """ coluna = input("Coluna 1..3: ")
                if coluna == "":
                    print("Você não digitou nada! Por favor, insira um valor válido.")
                    continue """
                if coluna != "1" and coluna != "2" and coluna != "3":
                    print("Coordenadas inválidas! Por favor, insira valores entre 1 e 3.")
                    continue
                coluna = int(coluna)
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
            # Identifica qual jogador venceu
            if simbolo == jogador1[1]:
                vencedor = jogador1[0]
                cor = jogador1[2]
            else:
                vencedor = jogador2[0]
                cor = jogador2[2]
            
            # Formata o nome e o símbolo com a cor, se definida
            if cor:
                nomeFormatado = cor + vencedor + END
                simboloFormatado = cor + simbolo + END
            else:
                nomeFormatado = vencedor
                simboloFormatado = simbolo

            print(" -- Venceu o jogador:", nomeFormatado, "que jogou com o símbolo", simboloFormatado)
            return simbolo
        elif verificaEmpate(galo):
            mostraTabuleiro(galo, 3, 3)
            print(" -- Empate!")
            return "empate"
    return None #returna nada para prevenir erros(é uma proteção do código)

# Definir variáveis de estatísticas fora do loop principal
empates = 0
opcao = 0
espaco = "\n"*3
pResumo ="9 - Ver resumo\n10 - Limpar os dados"
PSair = "12 - Sair"
PVoltar ="11 - Voltar ao menu anterior"
update=""
inputCores = "0 - PREDEFENIDO\n1 - AMARELO\n2 - AZUL\n3 - BRANCO\n4 - CIANO\n5 - ROXO\n6 - VERDE\n7 - VERMELHO\nEnumere a cor que deseja utilizar para os seus símbolos: "
menuTemporario=1
jogador1, jogador2 = inicializaJogadores()

# A RETIFICAR DEPOIS !
if jogador1[1] != "X" and jogador1[1] != "O":
    jogador1[1] = "X"
    
if jogador1[1] == "X":
    jogador2[1] = "O"
else:
    jogador2[1]= "X"


while True:
    opcao = menuJogo(jogador1[3], jogador2[3], empates, espaco,menuTemporario, update, jogador1[0], jogador2[0])

    # Programa principal
    galo = criaTabuleiro(3, 3, 0)
    galo = inicializaTabuleiro(galo, 3, 3, ' ')


    if opcao == 1: #1.1
        

        simboloJ1 = jogador1[1]  # Apenas "X"
        simboloJ2 = jogador2[1]  # Apenas "O"
        # ATÉ AQUI !


        while True: #Jogar enquanto os jogadores o entenderem  
            galo = inicializaTabuleiro(galo, 3, 3, '_')  # Limpa o tabuleiro

            # Realiza uma partida
            resultado = jogo(galo, simboloJ1, simboloJ2, espaco,jogador1, jogador2)
            # Atualiza estatísticas
            if resultado == simboloJ1:
                jogador1[3] += 1
            elif resultado == simboloJ2:
                jogador2[3] += 1
            elif resultado == "empate":
                empates += 1
            # Pergunta se deseja continuar jogando
            numeroDeJogos = jogador1[3]+jogador2[3]+empates

            while True :


                continuar = inputVazio("Deseja jogar novamente (S/N): ").upper() # permite assim reduzir bastante o codigo, visto que o que esta em comentario é escrito mais do que uma vez no codigo
                """ continuar = input("Deseja jogar novamente (S/N): ").upper()
                if continuar == "": # serve para prevenir que o utilizador nao entre um valor vazio
                    print("Você não digitou nada! Por favor, insira um valor válido.")
                    continue """
                if continuar != "S" and continuar != "N": # serve para prevenir que o utilizador nao entre um valor nao autorizado
                    print("Resposta inválidas! Por favor, insira valores S ou N.")
                    continue
                break
            
            if continuar == "N":
                
                print(espaco)
                print(jogador1[0], "têm", jogador1[3], " vitória(s),", (jogador1[3] / (numeroDeJogos)) * 100, "%")
                print(jogador2[0], "têm", jogador2[3], " vitória(s),", (jogador2[3] / (numeroDeJogos)) * 100, "%")
                print("Empates:", empates, ",", (empates / numeroDeJogos) * 100, "%") 
                break
            else: 
                print(espaco)# Turna o jogo mais "limpo", mostrando só o tabuleiro


            """ # Opcional: alterna os símbolos para a próxima partida
            simboloJ1, simboloJ2 = simboloJ2, simboloJ1 """
            # Em vez de trocar apenas os símbolos, troque os dados completos:
            if resultado == simboloJ1:
                jogador1, jogador2 = jogador2, jogador1
                simboloJ1 = jogador1[1]
                simboloJ2 = jogador2[1]



        
    elif opcao == 7:

        print(espaco)# Turna o jogo mais "limpo"
        resumo(jogador1[0], jogador2[0], jogador1[3], jogador2[3], empates)

        
    elif opcao == 8:

        print(espaco)# Turna o jogo mais "limpo"
        print("Os dados foram todos colocados com os valores padroes de inicio.")
        jogador1, jogador2 = inicializaJogadores()
     


    elif opcao == 9:
        print(espaco)# Turna o jogo mais "limpo"
        print("A sair do jogo....")

        resumo(jogador1[0], jogador2[0], jogador1[3], jogador2[3], empates)


        break


    else:
        print("Opção inválida")


#1 7 8 9