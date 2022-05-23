import re
import itertools

def armazena_gabarito():

    '''
    Armazena o gabarito da prova. Retorna o gabarito.
    '''

    questoes = '''
    01	    06	 	 	 	 X	 	 	 	 08
    02	 	05	 	 X	 X	 	 	 	 	 06
    03	 	06	 X	 X	 	 X	 	 X	 	 43
    04	 	05	 X	 	 	 	 X	 	 	 17
    05	 	07	 	 	 	 X	 X	 	 X	 88
    06	 	07	 X	 X	 X	 X	 	 X	 	 47
    07	 	06	 X	 X	 X	 	 	 	 	 07
    08	 	06	 	 X	 X	 X	 	 	 	 14
    09	 	07	 	 	 X	 	 X	 	 X	 84
    10	 	06	 X	 	 	 	 	 X	 	 33
    11	 	06	 X	 X	 	 	 X	 X	 	 51
    12	 	06	 	 X	 X	 X	 X	 	 	 30
    13      06	 X	 	 	 	 X	 X	 	 49
    14	 	05	 	 	 X	 	 X	 	 	 20
    15	 	06	 	 	 	 X	 	 X	 	 40
    16	 	06	 X	 X	 	 X	 	 	 	 11
    17	 	06	 X	 X	 	 X	 	 X	 	 43
    18	 	06	 X	 X	 	 	 	 	 	 03
    19	 	05	 	 	 	 X	 X	 	 	 24
    20	 	05	 	 X	 X	 	 	 	 	 06
    21	    04	 X	 X	 	 X	 	 	 	 11
    22	 	04	 X	 X	 X	 	 	 	 	 07
    23	 	                                 11
    24	 	05	 X	 	 	 X	 X	 	 	 25
    25	 	05	 X	 X	 X	 	 X	 	 	 23
    26	 	05	 X	 	 X	 	 X	 	 	 21
    27	 	06	 	 	 X	 X	 X	 	 	 28
    28	 	05	 	 	 X	 	 	 	 	 04
    29	 	05	 X	 	 	 X	 	 	 	 09
    30	 	04	 X	 	 	 X	 	 	 	 09
    31	    06	 X	 	 X	 	 	 	 	 05
    32	 	07	 	 X	 	 	 	 X	 	 34
    33	 	06	 	 X	 X	 	 	 	 	 06
    34	 	06	 	 X	 	 X	 X	 	 	 26
    35	 	07	 	 	 	 	 	 	 X	 64
    36	 	07	 X	 	 	 	 X	 	 X	 81
    37	 	04	 	 	 X	 	 	 	 	 04
    38	 	06	 X	 	 	 	 X	 X	 	 49
    39	 	06	 	 	 	 X	 	 X	 	 40
    40	 	06	 X	 X	 X	 X	 	 X	 	 47'''

    return questoes

def repostas(x):

    '''
    Recebe um inteiro que corresponde a resposta somatória. Consulta as alternativas possiveis (já configurada) e imprime a combinação que somada que forma o numero da entrada.
    '''

    lista_respostas_possiveis = [1, 2, 4, 8, 16, 32, 64]
    combinacao = []
    for index in range(len(lista_respostas_possiveis)):
        for seq in itertools.combinations(lista_respostas_possiveis, index):
            if sum(seq) == x:
                combinacao.append(seq)
    print(f'As alternativas a serem assinaladas são: {combinacao}')

def main_conferencia():

    '''
    Recebe um input do usuário informando qual a pergunta que ele quer consultar o gabarito.
    Imprime a resposta e as combinações que forma a resposta.
    '''

    while True:
        anwser = int(input('\nDigite o numero da questão para ver a resposta: '))    
        catch = re.split(r'\n', armazena_gabarito())

        transform = str(catch[anwser])
        print(transform)

        if 'X' in transform: 
            convert_in_int = int(transform[-2:])
            repostas(convert_in_int) 

main_conferencia()

	