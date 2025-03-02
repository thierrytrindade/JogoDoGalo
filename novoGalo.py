VARIAVEIS


1. Variáveis para o Tabuleiro
tabuleiro:
Um array bidimensional (lista de listas) de tamanho 3x3 para representar a grade do jogo.
Exemplo:
python
Copiar
tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
2. Variáveis para os Jogadores
Cada jogador pode ser representado por um array unidimensional, onde cada posição tem um significado definido. Por exemplo:

jogador1:
Índice 0: nome
Índice 1: símbolo
Índice 2: cor
Índice 3: vitórias
Exemplo:

python
Copiar
jogador1 = ["Maria", "X", "azul", 0]
jogador2:
Mesma estrutura que o jogador1
Exemplo:

python
Copiar
jogador2 = ["João", "0", "vermelho", 0]
Observação: Lembre-se de comentar o código deixando claro qual índice representa cada informação para manter a legibilidade.

3. Variáveis de Controle do Jogo
jogador_atual:
Pode ser um número (por exemplo, 1 ou 2) para indicar de quem é a vez de jogar ou, alternativamente, o próprio símbolo.

contador_jogadas:
Um inteiro que conta o número de jogadas realizadas. Isso ajuda a limitar o jogo a 9 jogadas.

resultado:
Uma variável para armazenar o estado do jogo, por exemplo, "vitória", "empate" ou um identificador específico para o vencedor.

4. Variáveis para Funcionalidades Adicionais
modo_jogo:
Variável para definir se o jogo é jogador vs jogador ou jogador vs computador.

total_jogos:
Para batalhas (melhor de 3, melhor de 5 ou personalizado), definindo o número total de partidas.

sinal_interrupcao:
Um caractere ou valor que, quando inserido, interrompe a partida atual e concede a vitória ao adversário.

Resumo das Variáveis
Tabuleiro:

tabuleiro (lista bidimensional 3x3)
Jogadores (para cada jogador):

jogador1 = [nome, símbolo, cor, vitórias]
jogador2 = [nome, símbolo, cor, vitórias]
Controle do Jogo:

jogador_atual
contador_jogadas
resultado
Funcionalidades Extras:

modo_jogo
total_jogos
sinal_interrupcao