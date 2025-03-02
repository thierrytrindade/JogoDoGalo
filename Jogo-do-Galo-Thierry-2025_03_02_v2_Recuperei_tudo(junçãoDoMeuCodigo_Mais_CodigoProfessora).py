#Jogo do Galo
#Rotinas
"""
Estrutura de dados
Matriz 3x3 | vetor 9 elementos
num_vitorias por jogador, num_empates

criar a matriz/vetor 
inicializar a matriz(tabuleiro de jogo)
mostrar a matriz (tabuleiro de jogo)
mostrar menu do jogo
Ler uma jogada e preencher o tabuleiro
verificar se após jogada alguém ganhou
atualizar a pontuação do jogo
questionar se querem voltar a jogar (novo jogo)

"""




#falta empates




def criaTabuleiro(l, c, v): #l linhas....
    m=[]
    for i in range(l):
        linha=[]
        for j in range(c):
            linha+=[v]
        m+=[linha]
    return m # retornar a matriz, preenchida com valor em v

def inicializaTabuleiro(m, l, c, valor):
    #para cada linha
    for i in range(l):
        #percorre todas as colunas e coloca o valor
        for j in range(c):
            m[i][j]=valor
    return m

def mostraTabuleiro(m, l, c):
    for i in range(l):
        for j in range(c):
            print(m[i][j], end=' ');
        print()

def menuJogo():
    print(".... JOGO DO GALO ....");
    print("1 - Jogar");
    print("2 - Sair");
    op=int(input("Escolha uma opção: "));
    return op;

def verificaVencedor(tabuleiro, simbolo):
    #Recebe por parametro o tabuleiro de jogo(matriz galo) e o simbolo do jogador atual
    #O jogador vence em linha e coluna
    for i in range(0, 3):
        if (tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2]==simbolo) or (tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i]==simbolo):
            return True; 
    #O jogador vence na diagonal
    if (tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2]==simbolo) or (tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0]==simbolo):
        return True; 
    return False;

def jogo(galo, simbolo, sJ1, sJ2): # permite jogar 1 vez
    for i in range(0,9):
        mostraTabuleiro(galo, 3, 3);
        if i%2 == 0: #jogada par->Jogador X
            simbolo = sJ1; 
            #auxj1 = simbolo
        else:
            simbolo = sJ2; 
            #auxj2 = simboloJ2;
        #validar a jogada
        while True:
            #ler jogada por coordenadas da matriz
            print("\nJogador ", simbolo);
            linha = int(input("Linha 1..3:"));
            coluna = int(input("Coluna 1..3:"));
            # verifica as coordenadas da jogada estão livres
            if galo[linha-1][coluna-1]=='_':
                galo[linha-1][coluna-1]=simbolo;
                break; #interrompe o ciclo de validação da jogada
            else: 
                print("\n------ Posição ocupada, escolha outra!!!\n");
        #verificar se há vencedor
        if verificaVencedor(galo, simbolo) :
            print(" -- Venceu o jogador :", simbolo);
            return simbolo;
    return simbolo; 
           
    #Mostra o tabuleiro final do jogo
    mostraTabuleiro(galo, 3, 3);


#Programa principal
galo=criaTabuleiro(3,3,0) 
galo = inicializaTabuleiro(galo, 3, 3,'_')
#definir o simbolo dos jogadores para alternar entre os jogadores
simboloJ1 ='X';
simboloJ2 ='O';
simbolo = simboloJ1;
# variaveis para os jogadores(1 e 2) e o computador
Jogador1=[input("Nome do primeiro jogador: "),input("Qual simbolo que quere utilizar(X ou O): ").upper(),0]#nome do jogador,simbolo e depois as vitorias, para pedir o nome-> jogador1[0], simbolo-jogsdor1[1] e as vitorias->jogador1[2]
escolha=int(input("\t1---> para jogar com outra pessoa\n\t2---> para jogar com o computador\nopção: "))
if escolha==1:
    Jogador2=[input("Nome do segundo jogador: "),"O" if Jogador1[1]=="X" else "X",0]#nome do jogador,simbolo e depois as vitorias, para pedir o nome-> jogador2[0], simbolo-jogsdor2[1] e as vitorias->jogador2[2] 
else:
    Jogador2=["Computador",0]#nome do jogador, e depois as vitorias, para pedir o nome-> jogador2[0], simbolo-jogsdor2[1] e as vitorias->jogador2[2]
simboloJ1 = Jogador1[1];
simboloJ2 = Jogador2[1];
while True:
    op=menuJogo();
    if op == 1:# Jogo 
        while True: #Jogar enquanto os jogadores o entenderem   
            galo = inicializaTabuleiro(galo, 3, 3,'_') #Limpar o tabuleiro de jogo
            #mostraTabuleiro(galo, 3, 3);
            

            #contar vitorias
            simbolo = jogo(galo, simbolo, simboloJ1, simboloJ2);
            # simbolo contem o simbolo do vencedor
            if simbolo == simboloJ1:
                Jogador1[2]+=1
            if simbolo == simboloJ1:
                Jogador2[2]+=1


            mostraTabuleiro(galo,3,3)
            continuar= input("Deseja jogar novamente (S/N)").upper
            if continuar == "N":
                break;
            if simbolo == 'O':
                simboloJ1 = 'X';
                simboloJ2 = 'O';  
            else: 
                simboloJ1 = 'O';
                simboloJ2 = 'X';
                
    elif op==2:
        #mostra resumo do jogo se existir
        #Sair
        print("A sair do jogo....")
        break;
    else: #outra opção
        print('Opção inválida');
        



