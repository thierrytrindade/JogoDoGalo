
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
        ["Jogador 1", "X", AZUL, 0],
        ["Jogador 2", "O", VERDE, 0]
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

""" def mostraTabuleiro(tabuleiro, linha, coluna):
    for i in range(linha):
        for j in range(coluna):
            print(tabuleiro[i][j], end=' ')
        print() """

def mostraTabuleiro(tabuleiro, linha, coluna, jogador1, jogador2):
    for i in range(linha):
        for j in range(coluna):
            celula = tabuleiro[i][j]
            # Verifica se a célula é um dos símbolos dos jogadores e aplica a cor
            if celula == jogador1[1]:
                print(jogador1[2] + celula + END, end=' ')
            elif celula == jogador2[1]:
                print(jogador2[2] + celula + END, end=' ')
            else:
                print(celula, end=' ')
        print()

        







def menuJogo(vitorias1, vitorias2, empates,espaco,pSair):
    largura_total = 60
    temResumo = vitorias1 + vitorias2 + empates
    print(espaco)
    if temResumo == 0:
        opcoesValidas = ("1", "2", "9")
    else:
        opcoesValidas = ("1", "2", "7", "8", "9")
    while True:
        
        print("\t╔" + "═" * (largura_total - 2) + "╗") 
        print("\t║" +(NEGRITO+"JOGO DO GALO"+END).center(largura_total + 6) + "║")
        print("\t║" +"      1 - Jogar       ".center(largura_total - 2) + "║")
        print("\t║" +"   2 - Personalizar   ".center(largura_total - 2) + "║")
        print(pSair)
        print("\t╚" + "═" * (largura_total - 2) + "╝")

        opcao = input("Escolha uma opção: ")

        if opcao not in opcoesValidas:
            print(espaco)
            print("Entrada inválida! Por favor, insira um número válido.")
            """ continue """
        else :
            opcao=int(opcao) #em vez de meter no input meto aqui, assim consigo fazer a verificação de se o valor introduzido no codigo é simplesmente um enter ou nao, pois metendo in(input(...)) caso que a pessoa simplesmente fizesse enter dava logo erro fechando o programa e a ideia é podermos verificar e permitir ao utilizador de retificar os seus erros sem ter que ter que andar sempre a abrir o programa de novo apos um erro e assim nao tendo que voltar a fazer tudo o que ja tinha feito antes e que foi perdido pelo programa se fechar
            return opcao








def menuJogo(vitorias1, vitorias2, empates,espaco,menuTemporario, update, jogador1, jogador2,largura_total):
    pResumo ="7 - Ver resumo\n8 - Limpar os dados"
    pSair = "\t║" +"       9 - Sair       ".center(largura_total - 2)+ "║"
    pVoltar ="\t║" +"        9 - Voltar ao menu anterior       ".center(largura_total - 2)+ "║"


    AMARELO = "\033[1;33m"  
    END = "\033[0m"
    NEGRITO="\033[1m"
    largura_total = 60




    temResumo = vitorias1 + vitorias2 + empates
    print(espaco)

    while True:
        if menuTemporario==1:
            opcoesValidas = ("1", "2", "9")
                
            print(espaco)
            print("\t╔" + "═" * (largura_total - 2) + "╗") 
            print("\t║" +(NEGRITO+"JOGO DO GALO"+END).center(largura_total + 6) + "║")
            print("\t║" +"      1 - Jogar       ".center(largura_total - 2) + "║")
            print("\t║" +"   2 - Personalizar   ".center(largura_total - 2) + "║")
            print(pSair)
            print("\t╚" + "═" * (largura_total - 2) + "╝")

        if menuTemporario==2:
            opcoesValidas = ("1", "2", "3", "4", "9")
                       
            print(espaco)
            print("\t╔" + "═" * (largura_total - 2) + "╗") 
            print("\t║" + (NEGRITO+" => Jogar "+END).center(largura_total + 6) + "║")
            print("\t║" + "      1 - Partida simples/indefinida      ".center(largura_total - 2) + "║")
            print("\t║" + "              2 - Melhor de 3             ".center(largura_total - 2) + "║")
            print("\t║" + "              3 - Melhor de 5             ".center(largura_total - 2) + "║")
            print("\t║" + "    4 - Personalizar o número de jogos    ".center(largura_total - 2) + "║")
            print(pVoltar)
            print("\t╚" + "═" * (largura_total - 2) + "╝")
            
        if menuTemporario==3:
            opcoesValidas = ("1", "2", "3", "4", "5", "6", "9")
                
            print(espaco)
            if update !="" :
                print("\t "+(">>> "+update+" <<<").center(largura_total + 6))
            print("\t╔" + "═" * (largura_total - 2) + "╗") 

            print("\t║" + (NEGRITO+" => Personalizar "+END).center(largura_total + 6) + "║")
            print("\t║" + ("1 - Mudar nome do(a) " + jogador1).center(largura_total - 2) + "║" )
            print("\t║" + ("2 - Mudar cor do(a) " + jogador1).center(largura_total - 2) + "║" )
            print("\t║" + ("3 - Mudar nome do(a) " + jogador2).center(largura_total - 2) + "║" )
            print("\t║" + ("4 - Mudar cor do(a) " + jogador2).center(largura_total - 2) + "║" )
            print("\t║" + "5 - Mudar Simbolo de jogo".center(largura_total - 2) + "║" )
            print("\t║" + "6 - Mudar Simbolo para desistir".center(largura_total - 2) + "║" )
            print(pVoltar)
            print("\t╚" + "═" * (largura_total - 2) + "╝")

        
        opcao = inputVazio("Escolha uma opção: ")

        if opcao not in opcoesValidas:
            print(espaco)
            print("Entrada inválida! Por favor, insira um número válido.")
        else : 


            if opcao == "9" and menuTemporario !=1 : menuTemporario = 1

            elif opcao == "9" and menuTemporario ==1 : opcao=int(opcao); return 9, 1

            elif menuTemporario == 1 and opcao == "1" : menuTemporario = 2
            
            elif menuTemporario == 1 and opcao == "2" : menuTemporario = 3

            #elif opcao == 9 and menuTemporario == 2 : menuTemporario = 1
            

            elif menuTemporario == 2 and opcao == "1":
                opcao = int(opcao)
                return 1, 1

            elif menuTemporario == 2 and opcao == "2":
                opcao = int(opcao)
                return 1, 3

            elif menuTemporario == 2 and opcao == "3":
                opcao = int(opcao)
                return 1, 5

            elif menuTemporario == 2 and opcao == "4":
                opcao = int(opcao)
                return 1, 2
            

            elif menuTemporario == 3 and opcao == "1" : opcao="2"; opcao=int(opcao); return 2, 1

            elif menuTemporario == 3 and opcao == "2" : opcao="3"; opcao=int(opcao); return 3, 1

            elif menuTemporario == 3 and opcao == "3" : opcao="4"; opcao=int(opcao); return 4, 1

            elif menuTemporario == 3 and opcao == "4" : opcao="5"; opcao=int(opcao); return 5, 1

            elif menuTemporario == 3 and opcao == "5" : opcao="6"; opcao=int(opcao); return 6, 1

            elif menuTemporario == 3 and opcao == "6" : opcao="7"; opcao=int(opcao); return 7, 1
            



            
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

def jogo(galo, sJ1, sJ2, espaco, jogador1, jogador2, desistir):##########################################################################################################################################
    VERMELHO = "\033[1;31m"
    VERDE = "\033[1;32m"  
    END = "\033[0m"
    for i in range(9):
        mostraTabuleiro(galo, 3, 3, jogador1, jogador2)
        # Alterna entre os jogadores
        if i % 2 == 0:
            simbolo = sJ1
            turno = jogador1 #turno é quem joga
            oponente = jogador2
        else:
            simbolo = sJ2
            turno = jogador2
            oponente = jogador1

        # Validação da jogada
        print("\nJogador", turno[0], "(", simbolo, ")")
        while True:        
            while True :
                linha = inputVazio("Linha 1..3 (ou desistir): ")
                if linha == desistir:
                    print(f"\n=> {turno[0]} {VERMELHO}desistiu!{END} {oponente[0]} {VERDE}vence por desistência!{END}")
                    return oponente[1]  # Retorna o símbolo do oponente como vencedor
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
                mostraTabuleiro(galo, 3, 3, jogador1, jogador2)
                print("\nJogador", simbolo)#repito a chamada do jugador, pois como faço 130 linhas para continuar a saber qual o jogador a jogar
                
        # Verifica se houve vencedor
        if verificaVencedor(galo, simbolo):
            mostraTabuleiro(galo, 3, 3, jogador1, jogador2)
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

            print("\n=> Venceu o jogador:", nomeFormatado, "que jogou com o símbolo", simboloFormatado)
            return simbolo
        elif verificaEmpate(galo):
            mostraTabuleiro(galo, 3, 3, jogador1, jogador2)
            print(" -- Empate!")
            return "empate"
    return None #returna nada para prevenir erros(é uma proteção do código)

# Definir variáveis de estatísticas fora do loop principal

largura_total = 60
empates = 0
opcao = 0
espaco = "\n"*3
pSair = "\t║" +"       9 - Sair       ".center(largura_total - 2)+ "║"
pVoltar ="\t║" +"        9 - Voltar ao menu anterior       ".center(largura_total - 2)+ "║"
update=""
inputCores = "0 - PREDEFENIDO\n1 - AMARELO\n2 - AZUL\n3 - BRANCO\n4 - CIANO\n5 - ROXO\n6 - VERDE\n7 - VERMELHO\nEnumere a cor que deseja utilizar para os seus símbolos: "
menuTemporario=1
jogador1, jogador2 = inicializaJogadores()
seriesLength = 0  # valor default; troque conforme a escolha do usuário
desistir = "9"

# A RETIFICAR DEPOIS !
if jogador1[1] != "X" and jogador1[1] != "O":
    jogador1[1] = "X"
    
if jogador1[1] == "X":
    jogador2[1] = "O"
else:
    jogador2[1]= "X"


while True:
    opcao, seriesLength = menuJogo(jogador1[3], jogador2[3], empates, espaco, menuTemporario, update, jogador1[0], jogador2[0], largura_total)

    NEGRITO="\033[1m"
    # Programa principal
    galo = criaTabuleiro(3, 3, 0)
    galo = inicializaTabuleiro(galo, 3, 3, ' ')

# Suponha que a variável seriesLength seja definida a partir do menu.
# Por exemplo, se o usuário escolher:
#   "1" -> seriesLength = 1    (apenas uma partida)
#   "2" -> seriesLength = 3    (melhor de 3)
#   "3" -> seriesLength = 5    (melhor de 5)
#   "4" -> seriesLength = <valor customizado>
#
# Aqui mostramos a parte principal do jogo adaptada:

    if opcao == 1:
        # seriesLength define o número total de partidas para a série.
        # Se seriesLength == 1: é partida única; se > 1: é uma série.
        # Por exemplo, vamos supor que você já tenha obtido esse valor:
        
        if seriesLength > 1:
            # Calcula o número de vitórias necessárias para vencer a série
            if seriesLength == 2:
                while True :
                    seriesLength = int(inputVazio("Insira o número de partidas superior a 5: "))
                    if seriesLength < 6: # serve para prevenir que o utilizador nao entre um valor nao autorizado
                        print("Insira um valor superior a 5.")
                        continue
                    seriesLength = int(seriesLength) # serve para converter de string para int, visto que se eu tivesse int(input) nao deixava sequer pre1venir o primeiro passo de ver se o campo é vazio e o jogo fechava logo de uma vez
                    break
                
            winsNeeded = (seriesLength // 2) + 1 # // serve para recuperar o valor absoluto assim por exemplo se a pessoa meter 7 metade é 3.5, mas visto que nao da para ganhar 3.5 vezes recupero o valor absoluto 3 e adiciono +1 logo 4 o que é exatamente o maior de 7 e assim funciona com qualquer numero colocado pelo utilizador
            currentWins1 = 0
            currentWins2 = 0
            
            print(f"Iniciando série melhor de {seriesLength} (necessário {winsNeeded} vitórias).")
            
            while currentWins1 < winsNeeded and currentWins2 < winsNeeded:
                # Limpa o tabuleiro para a partida atual
                galo = inicializaTabuleiro(galo, 3, 3, '_')
                
                # Realiza uma partida
                resultado = jogo(galo, jogador1[1], jogador2[1], espaco, jogador1, jogador2, desistir)
                
                # Atualiza estatísticas gerais e da série
                if resultado == jogador1[1]:
                    jogador1[3] += 1
                    currentWins1 += 1
                    #print(f"{jogador1[0]} venceu a partida!")
                elif resultado == jogador2[1]:
                    jogador2[3] += 1
                    currentWins2 += 1
                    #print(f"{jogador2[0]} venceu a partida!")
                elif resultado == "empate":
                    empates += 1
                    print("Empate nesta partida!")

                # Se não houve empate, inverte a ordem para que o perdedor comece o próximo jogo.
                if resultado != "empate":
                    # Se o jogador que iniciou venceu, troca a ordem
                    if resultado == jogador1[1]:
                        jogador1, jogador2 = jogador2, jogador1
                        currentWins1, currentWins2 = currentWins2, currentWins1
                    # Se jogador2 venceu, o perdedor (jogador1) já está primeiro, então não precisa trocar
            
            # Verifica o vencedor da série
            if currentWins1 == winsNeeded:
                print(f"\n-- {jogador1[0]} venceu a série!")
            else:
                print(f"\n-- {jogador2[0]} venceu a série!")
            
            
            # Chama a função resumo para exibir as estatísticas finais
            resumo(jogador1[0], jogador2[0], jogador1[3], jogador2[3], empates)
            # Reset dos resultados de ambos os jogadores e empates
            jogador1[3] = 0
            jogador2[3] = 0
            empates = 0

            # Define o menuTemporario para 2, para que seja exibido o menu de "Jogar"
            menuTemporario = 2

        else:
            # Modo partida única (seriesLength == 1)
            while True:
                galo = inicializaTabuleiro(galo, 3, 3, '_')  # Limpa o tabuleiro
                
                # Realiza uma partida única
                resultado = jogo(galo, jogador1[1], jogador2[1], espaco, jogador1, jogador2, desistir)
                
                # Atualiza estatísticas gerais
                if resultado == jogador1[1]:
                    jogador1[3] += 1
                elif resultado == jogador2[1]:
                    jogador2[3] += 1
                elif resultado == "empate":
                    empates += 1
                
                numeroDeJogos = jogador1[3] + jogador2[3] + empates
                
                # Exibe placar após a partida
                print(f"\nPlacar atual: {jogador1[0]} - {jogador1[3]} x {jogador2[3]} - {jogador2[0]} | Empates: {empates}")
                
                # Pergunta se deseja continuar jogando partidas únicas
                continuar = inputVazio("Deseja jogar novamente (S/N): ").upper()
                if continuar != "S":
                    print(espaco)
                    """ print(f"{jogador1[0]} tiveram {jogador1[3]} vitória(s) ({(jogador1[3] / numeroDeJogos) * 100:.2f}%)")
                    print(f"{jogador2[0]} tiveram {jogador2[3]} vitória(s) ({(jogador2[3] / numeroDeJogos) * 100:.2f}%)") """
                    
                    resumo(jogador1[0], jogador2[0], jogador1[3], jogador2[3], empates)
                    #print(f"Empates: {empates} ({(empates / numeroDeJogos) * 100:.2f}%)")# Reset dos resultados de ambos os jogadores e empates
                    jogador1[3] = 0
                    jogador2[3] = 0
                    empates = 0

                    # Define o menuTemporario para 2, para que seja exibido o menu de "Jogar"
                    menuTemporario = 2
                    break
                else:
                    print(espaco)
                    # Se o jogador que venceu foi o primeiro, inverte a ordem para que o perdedor comece
                    if resultado == jogador1[1]:
                        jogador1, jogador2 = jogador2, jogador1
                        # Atualiza os símbolos para a nova ordem
                        simboloJ1 = jogador1[1]
                        simboloJ2 = jogador2[1]

    elif opcao == 2:  # 3.1wedsrawq
    # Dados dos jogadores: [nome, símbolo, vitórias]
        jogador1[0] = input("Nome do primeiro jogador: ")
        while jogador1[0] == "":
            print("Você não digitou nada! Por favor, insira um nome válido.")
            jogador1[0] = input("Nome do primeiro jogador: ")
        update = "Personalização efetuada : O nome do jogador 1 é " + jogador1[0]

        
        menuTemporario = 3

    

    elif opcao == 3:  # 3.2
        inputCor = int(input(inputCores))
        while inputCor == "":
            print("Você não digitou nada! Por favor, insira um valor válido.")
            inputCor = int(input(inputCores))

            
        if inputCor == 0 :
            jogador1[2]=PREDEFENIDO
            cor="Predefenido"
        if inputCor == 1 : 
            jogador1[2]=AMARELO
            cor="Amarelo"
        if inputCor == 2 :
            jogador1[2]=AZUL
            cor="Azul"
        if inputCor == 3 :
            jogador1[2]=BRANCO
            cor="Branco"
        if inputCor == 4 :
            jogador1[2]=CIANO
            cor="Ciano"
        if inputCor == 5 :
            jogador1[2]=ROXO
            cor="Roxo"
        if inputCor == 6 :
            jogador1[2]=VERDE
            cor="Verde"
        if inputCor == 7 :
            jogador1[2]=VERMELHO
            cor="Vermelho"
        update = "Personalização efetuada : A cor do(a) "+ jogador1[0]+" é " +jogador1[2]+cor+END
        menuTemporario = 3





    elif opcao == 4:  # 3.3
        jogador2[0] = input("Nome do primeiro jogador: ")
        while jogador2[0] == "":
            print("Você não digitou nada! Por favor, insira um nome válido.")
            jogador2[0] = input("Nome do primeiro jogador: ")
        update = "Personalização efetuada : O nome do jogador 2 é " + jogador2[0]
        menuTemporario = 3

    elif opcao == 5:  # 3.4
        inputCor = int(input(inputCores))
        while inputCor == "":
            print("Você não digitou nada! Por favor, insira um valor válido.")
            inputCor = int(input(inputCores))

            
        if inputCor == 0 :
            jogador2[2]=PREDEFENIDO
            cor="Predefenido"
        if inputCor == 1 : 
            jogador2[2]=AMARELO
            cor="Amarelo"
        if inputCor == 2 :
            jogador2[2]=AZUL
            cor="Azul"
        if inputCor == 3 :
            jogador2[2]=BRANCO
            cor="Branco"
        if inputCor == 4 :
            jogador2[2]=CIANO
            cor="Ciano"
        if inputCor == 5 :
            jogador2[2]=ROXO
            cor="Roxo"
        if inputCor == 6 :
            jogador2[2]=VERDE
            cor="Verde"
        if inputCor == 7 :
            jogador2[2]=VERMELHO
            cor="Vermelho"
        update = "Personalização efetuada : A cor do(a) "+ jogador2[0]+" é " +jogador2[2]+cor+END
        menuTemporario = 3

    elif opcao == 6:  # 3.5
        jogador1[1] = input("Qual símbolo que o " + jogador1[0] + " quer utilizar (X ou O): ").upper()
        while jogador1[1] == "":
            print("Você não digitou nada! Por favor, insira um símbolo válido.")
            jogador1[1] = input("Qual símbolo que o " + jogador1[0] + " quer utilizar (X ou O): ").upper()
        jogador2[1] = "O" if jogador1[1] == "X" else "X"
        update = "Personalização efetuada : " + jogador1[0] + " está neste momento com o símbolo " + jogador1[1] + " e " + jogador2[0] + " está com " + jogador2[1]
        menuTemporario = 3
    
    
    elif opcao == 7:  # 3.5
        desistir = inputVazio("Qual símbolo que o que deseja usar para desistir : ")
        update = "Personalização efetuada : o simbolo de desistir foi alterado e agora é " + desistir
        menuTemporario = 3


    elif opcao == 9:
        print(espaco)# Turna o jogo mais "limpo"
        print("A sair do jogo....")

        resumo(jogador1[0], jogador2[0], jogador1[3], jogador2[3], empates)
        print(espaco)





        print("\t╔" + "═" * (largura_total - 2) + "╗")
        print("\t║" + "🚀 O JOGO MAIS ÉPICO DE SEMPRE! 🚀".center(largura_total - 4) + "║")
        print("\t║" + "🎮  Desenvolvido por TT Games 🎮".center(largura_total - 4) + "║")
        print("\t╠" + "═" * (largura_total - 2) + "╣")
        print("\t║" + "🌟 Equipe de Desenvolvimento 2024 / 2025 🌟".center(largura_total - 4) + "║")
        print("\t╠" + "═" * (largura_total - 2) + "╣")
        print("\t║" + "Disciplina Aplicações Informaticas B".center(largura_total - 2) + "║")
        print("\t║" + "Turma 12B".center(largura_total - 2) + "║")
        print("\t║" + "Thierry 'Chefe Supremo' Trindade".center(largura_total - 2) + "║")
        print("\t║" + "Santiago 'O' Santos".center(largura_total - 2) + "║")
        print("\t║" + "Andre 'Ratazana' Madail".center(largura_total - 2) + "║")
        print("\t╠" + "═" * (largura_total - 2) + "╣")
        print("\t║" + "🕵️  Testadores".center(largura_total - 1) + "║")
        print("\t║" + "Professor com paciência infinita".center(largura_total - 2) + "║")
        print("\t╠" + "═" * (largura_total - 2) + "╣")
        print("\t║" + "🛠️  Engine & Ferramentas Utilizadas".center(largura_total - 1) + "║")
        print("\t║" + "Desenvolvido em Python 🐍".center(largura_total - 3) + "║")
        print("\t║" + "Google & CTRL+C / CTRL+V".center(largura_total - 2) + "║")
        print("\t╠" + "═" * (largura_total - 2) + "╣")
        print("\t║" + "🙌  Agradecimentos Especiais".center(largura_total - 3) + "║")
        print("\t║" + "Google, Wikipedia e tutoriais infinitos".center(largura_total - 2) + "║")
        print("\t║" + "CTRL+Z, salvando vidas desde sempre".center(largura_total - 2) + "║")
        print("\t║" + "Impulsionado por café e ansiedade! ☕😖".center(largura_total - 4) + "║")
        print("\t╠" + "═" * (largura_total - 2) + "╣")
        print("\t║" + "🎖️    Mensagem Final     ".center(largura_total - 1) + "║")
        print("\t║" + "\"Obrigado por jogar e aguentar os bugs!\"".center(largura_total - 2) + "║")
        print("\t║" + "Sair...".center(largura_total - 2) + "║")
        print("\t╚" + "═" * (largura_total - 2) + "╝")#Texto[Aquele que quero centralizar].center(largura[tamanho da largura total menos as bordas e tambem os emogis, pois ocupam mais de um espaço], caractere_de_preenchimento[Tem como predefenido o espaço se caso de não preenchimento]).
        #retirei os emogis do link:https://en.wikipedia.org/wiki/List_of_emojis


        break

    else:
        print("Opção inválida")