import time

class Compara_buscas:

    def busca_binaria(self, lista, elemento_procurado):

        '''
        Recebe uma lista e um elemento a ser procurado. Caso encontre ele retorna o index do elemento,
        caso não encontre ele retorna -1.

        Este código não é de minha autoria, créditos ao pessoal da USP/SP. Só dei uma alterada para
        retornar o -1 caso o elemento_procurado não estiver na lista.

        Utiliza o método de busca binária. Em linhas gerais, vai "particionado" a lista até encontrar/ou não
        o elemento. É de suma importância que a lista esteja organizada em ordem crescente.
        '''

        primeiro = 0
        ultimo = len(lista) - 1

        while primeiro <= ultimo:
            
            meio = (primeiro + ultimo) // 2
       
            if lista[meio] == elemento_procurado:
                return meio

            else:
                if elemento_procurado > lista[meio]:
                    primeiro = meio + 1
                else: 
                    ultimo = meio - 1                

        return -1

    def busca_sequencial(self, lista, elemento_procurado):

        '''
        Recebe uma lista e um elemento a ser procurado. Caso encontre ele retorna o index do elemento,
        caso não encontre ele retorna -1
        '''

        for index in range(len(lista)):
                if lista[index] == elemento_procurado:
                    return index
 
        return -1

    def main(self, lista, elemento_procurando):

        '''
        Utilização principal dos métodos. Retorna qual deles foi mais rápido.
        '''

        #É importante que a lista esteje ordenada para a busca binária ter exito.
        self.lista = lista
        self.elemento_procurado = elemento_procurando

        antes = time.time()
        self.busca_binaria(self, lista, elemento_procurado)
        depois = time.time()

        tempo_execução_bi = depois - antes

        antes = time.time()
        self.busca_sequencial(self, lista, elemento_procurado)
        depois = time.time()

        tempo_execução_seq = depois - antes

        if tempo_execução_bi > tempo_execução_seq:
            return 'Busca binário foi mais rápido'
        else:
            return 'Busca sequencial foi mais rápido.'


### EXEMPLO DE UTILIZAÇÃO
lista = [x for x in range(4)] #A lista já sai ordenada.
elemento_procurado = 88

objeto = Compara_buscas
print(objeto.busca_binaria(objeto, lista, elemento_procurado))
