import random

class Meu_cartão_vazou:

    def trata_numero(self, numero):

        '''
        Recebe um int ou str e retorna um inteiro tratado.  
        '''

        lista_de_casos = [ ' ', '.', ',', '-', '_', '*', '+']
        num_tratado = str(numero)
    
        for x in range(len(lista_de_casos)):
            num_tratado = num_tratado.replace(lista_de_casos[x], '')
        return int(num_tratado)

    def cria_num_cartões(self, numero_digitos):

        '''
        Recebe um int e retorna um inteiro aleatório com quantidade determinada de digitos inserida na entrada.
        '''

        num = numero_digitos
        numero_end = ''

        for x in range(num):
            if x == 0:
                numero_end+= str(random.randint(1,9))
            else:
                numero_end+= str(random.randint(0,9))

        return int(numero_end)

    def cria_lista_int(self, numero_de_itens):
    
        '''
        Recebe um int referente a quantidade de itens que a lista que ira ser criada deve possuir e o quantidade 
        de digitos que os cartões fake devem ter. Retorna uma lista
        '''
        
        lista = []
        for x in range(numero_de_itens):
            lista.append(self.cria_num_cartões(self, 16))
        return lista

    def in_list(self, num_cartao, lista_cartoes):
    
        '''
        Retorna um Boolean se o cartão está ou não na lista.
        '''
        
        return num_cartao in lista_cartoes

    def main(self, num_card):
    
        '''
        Recebe o numero de um cartão e retorna se ele se encontra lista.
        Obs: Foi setado para ser criado uma lista ficticia de 6 cartões com 16 digitos cada um.
        '''
        
        cartão_tratado = self.trata_numero(num_card)
        lista_de_cartões = self.cria_lista_int(6) #Escolhi 6 aleatóriamente

        if self.in_list(cartão_tratado, lista_de_cartões):
            return "Opa!!! Meu cartão está no vazamento."
        else:
            return "Tudo certo, não fui vazado."
