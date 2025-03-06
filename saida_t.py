#Saida
PREDEFENIDO = ""
AMARELO = "\033[1;33m"   
AZUL = "\033[1;34m"      
BRANCO = "\033[1;37m"    
CIANO = "\033[0;36m"     
ROXO = "\033[1;35m"      
VERDE = "\033[1;32m"     
VERMELHO = "\033[1;31m"  
END = "\033[0m"  #Anula a formatação anterior
NEGRITO="\033[1m"
largura_total = 60

print("\t╔" + "═" * (largura_total - 2) + "╗")
print("\t║" + "🚀 O JOGO MAIS ÉPICO DE SEMPRE! 🚀".center(largura_total - 4) + "║")
print("\t║" + "🎮  Desenvolvido por TT Games 🎮".center(largura_total - 4) + "║")
print("\t╠" + "═" * (largura_total - 2) + "╣")
print("\t║" + "🌟 Equipe de Desenvolvimento 🌟".center(largura_total - 4) + "║")
print("\t╠" + "═" * (largura_total - 2) + "╣")
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

#Menu

#tirar
temResumo=1



largura_total = 60
pSair = "\t║" +"       9 - Sair       ".center(largura_total - 2)+ "║"
pVoltar ="\t║" +"        9 - Voltar ao menu anterior       ".center(largura_total - 2)+ "║"
espaco = "\n"*3
print(espaco)
print("\t╔" + "═" * (largura_total - 2) + "╗") 
print("\t║" +(NEGRITO+"JOGO DO GALO"+END).center(largura_total + 6) + "║")
print("\t║" +"      1 - Jogar       ".center(largura_total - 2) + "║")
print("\t║" +"   2 - Personalizar   ".center(largura_total - 2) + "║")
print(pSair)
print("\t╚" + "═" * (largura_total - 2) + "╝")





#menu2
print(espaco)
print("\t╔" + "═" * (largura_total - 2) + "╗") 
print("\t║" + (NEGRITO+" => Jogar "+END).center(largura_total + 6) + "║")
print("\t║" + "      1 - Partida simples/indefinida      ".center(largura_total - 2) + "║")
print("\t║" + "              2 - Melhor de 3             ".center(largura_total - 2) + "║")
print("\t║" + "              3 - Melhor de 5             ".center(largura_total - 2) + "║")
print("\t║" + "    4 - Personalizar o número de jogos    ".center(largura_total - 2) + "║")
print(pVoltar)
print("\t╚" + "═" * (largura_total - 2) + "╝")



#Menu 3
jogador1="Velcro"
jogador2="kmkdnkfn"
update="jbdusgaofug"


print(espaco)
print(AMARELO+update+END)
print("\t╔" + "═" * (largura_total - 2) + "╗") 

print("\t║" + (NEGRITO+" => Personalizar "+END).center(largura_total + 6) + "║")
print("\t║" + ("1 - Mudar nome do(a) " + jogador1).center(largura_total - 2) + "║" )
print("\t║" + ("2 - Mudar cor do(a) " + jogador1).center(largura_total - 2) + "║" )
print("\t║" + ("3 - Mudar nome do(a) " + jogador2).center(largura_total - 2) + "║" )
print("\t║" + ("4 - Mudar cor do(a) " + jogador2).center(largura_total - 2) + "║" )
print("\t║" + "5 - Mudar Simbolo".center(largura_total - 2) + "║" )
print(pVoltar)
print("\t╚" + "═" * (largura_total - 2) + "╝")