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