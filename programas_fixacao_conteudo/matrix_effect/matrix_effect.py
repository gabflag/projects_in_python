import random
import time

def cria_linha():

    '''
    Cria uma string de binários e retorna essa string. 
    '''

    line = ""
    for account in range(70):
        num = str(random.randint(0,1))+ ' '
        line+=num

    return line

def cria_lista_para_alterações(qnt_alteracoes, linha):

    '''
    Cria uma lista de index aleatórios os quais podem ser alterados em uma determinada string, leva em consideração 
    apenas letras/numeros. Recebe a quantidade de index para alterações e a própria string.
    Retorna essa lista com os index que podem ser alterados
    ''' 

    in_list = list(linha)
    lista_index_alteracoes = []
    for x in range(qnt_alteracoes):

        mantem_laco = True

        while mantem_laco:

            elemento = random.randint(0, len(linha)-1)

            if elemento not in lista_index_alteracoes and in_list[elemento] != ' ':
                lista_index_alteracoes.append(elemento)
                mantem_laco = False

    return lista_index_alteracoes

def altera_linha(lista_alteracoes, linha):

    '''
    Recebe uma lista de index e uma string.
    Imprimi a string de entrada alterada em um intervalor de 0.05 segundos.
    '''
    
    in_list = list(linha)
    for index in range(len(lista_alteracoes)):
        valor_index_alterado = lista_alteracoes[index]
        in_list[valor_index_alterado] = ' '

    linha_preparada = "".join(in_list)
    time.sleep(0.05)
    print(linha_preparada)
    
def chama_matrix():

    '''
    Define a quantidade de linhas que a matrix devera ter e chama as outras funções.
    '''

    qnt = 200

    for cont in range(qnt):

        linha = cria_linha()

        if cont < qnt // 6:
            lista_alt = cria_lista_para_alterações(20, linha)
            altera_linha(lista_alt, linha)

        elif cont < qnt // 4:
            lista_alt = cria_lista_para_alterações(30, linha)
            altera_linha(lista_alt, linha)
        
        elif cont < qnt // 2: 
            lista_alt = cria_lista_para_alterações(40, linha)
            altera_linha(lista_alt, linha)
        
        elif cont < qnt // 1.5: 
            lista_alt = cria_lista_para_alterações(50, linha)
            altera_linha(lista_alt, linha)
            
        elif cont < qnt // 1.1: 
            lista_alt = cria_lista_para_alterações(60, linha)
            altera_linha(lista_alt, linha)

            
    phrase_1 = 'The Matrix'
    print(f'\n\n{phrase_1.center(140)}\n\n')
    time.sleep(3)
    phrase_2 = 'Just binaries'
    print(f'\n{phrase_2.center(142)}\n')
    time.sleep(3)
    

def main():
    resposta = input('Do you want to know the matrix? (Yes or No) ').replace(' ', '')

    if resposta.lower() == "yes":
        time.sleep(0.5)
        print('\n\nOk, follow me until the rabbit hole!\n\n.\n.\n.\n')
        time.sleep(2)
        chama_matrix()
    else:
        print('ok')

main()
