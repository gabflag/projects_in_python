def apresenta_matriz(matriz,num_linhas):

    '''
    Imprime a matriz em um formato mais legivel para a partida.. Retorna um print
    '''

    for linha in range(num_linhas):
        print(matriz[linha])

def regras(matriz,simb):

    '''
    Estabele as regras para definir qual jogador é vencedor. Retorna um boolean.
    '''

    # Linhas horizontais

    if matriz[0][0] == simb and matriz[0][1] == simb and matriz[0][2] == simb:
        return True
    elif matriz[1][0] == simb and matriz[1][1] == simb and matriz[1][2] == simb:
        return True
    elif matriz[2][0] == simb and matriz[2][1] == simb and matriz[2][2] == simb:
        return True

    #Linhas Verticais
    elif matriz[0][0] == simb and matriz[1][0] == simb and matriz[2][0] == simb:
        return True
    elif matriz[0][1] == simb and matriz[1][1] == simb and matriz[2][1] == simb:
        return True
    elif matriz[0][2] == simb and matriz[1][2] == simb and matriz[2][2] == simb:
        return True
    
    #Linhas diagonais

    elif matriz[0][0] == simb and matriz[1][1] == simb and matriz[2][2] == simb:
        return True
    elif matriz[0][2] == simb and matriz[1][1] == simb and matriz[2][0] == simb:
        return True
    
    else:
        print()

def jogada(matriz,simb):

    '''
    Pergunta para o usuário qual será a sua jogada e altera a matriz. Retorna a matriz alterada.
    '''

    matriz_alterada = matriz
    apresenta_matriz(matriz_alterada,3)
    jogada_valida = False

    while jogada_valida != True:
        linha_alt = int(input("\nLinha a ser alterada: "))
        coluna_alt = int(input("Coluna a ser alterada: "))

        if type(coluna_alt) == int and type(linha_alt) == int:
            matriz[linha_alt][coluna_alt] = simb
            apresenta_matriz(matriz_alterada,3)
            jogada_valida = True
            
        else:
            print('\n\nATENÇÃO. Ocorreu um erro. Digite um numero inteiro pertencente ao Index.\n\n')

    return matriz_alterada

def main():

    print('''\n###########################\n\nBem vindo ao jogo da velha, para começarmos defina o símbolo utilizado por cada jogador.\n\n###########################\n''')

    matriz = []
    for linha in range(3):
        linha = []
        for colunas in range(3):
            linha.append('#')
        matriz.append(linha)

    apresenta_matriz(matriz,3)

    simb_1 = input('\nQual o símbolo que você pretende usar usário 1: ').replace(' ','')
    simb_2 = input('Qual o símbolo que você pretende usar usário 2: ').replace(' ','')
    
    print('\nPara ficar claro, diga qual linha e qual coluna você pretende alterar(Utilizar: 0, 1 ou 2). Vamos começar!\n')


    ########    PARTIDA     #########

    jogo_acabou = False    
    while jogo_acabou != True:

        #### Usuário 1 joga ####
        usu1_jogou = False
        deu_velha = 0

        while usu1_jogou != True:
            jogada(matriz,simb_1)
            deu_velha+=1
            jogo_acabou = regras(matriz, simb_1)
        
            if jogo_acabou:
                print('\nUsuário 1 ganhou a partida. Parabéns')
            elif deu_velha == 9:

                print('Deu velha, acabou a partida.')
                jogo_acabou = True
            
            else:
                print('')

            usu1_jogou = True

            #### Usuário 2 joga ####

            if jogo_acabou != True:
                print("Vez do Usuario 2, vamos lá!")
                jogada(matriz,simb_2)
                deu_velha+=1
                jogo_acabou = regras(matriz,simb_2)

                if jogo_acabou:
                    print('\nUsuário 2 ganhou a partida. Parabéns')

                elif deu_velha == 9:       
                    print('Deu velha, acabou a partida.')               
                    
                    jogo_acabou = True
                else:
                    print('\nVez do usuário 1')
                    usu1_jogou = False
            else:
                print('Fim')

main()
