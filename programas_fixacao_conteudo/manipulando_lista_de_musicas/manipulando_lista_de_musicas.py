class Lista_de_Musicas:

    def __init__(self, banda, musica):
        
        '''
        Método construtor da classe.
        '''
        self.banda =  banda
        self.musica = musica
    
    def busca_musica(self, musica, lista):

        '''
        Busca se a música se encontra na lista atual. Recebe uma string e a lista a ser comparada.
        Retorna um boolean.
        '''

        found_music = False

        for index in range(len(lista)):
            if (lista[index][1]).lower == musica.lower():
                print(f'Encontei sua musica, ela está na posição {index} da sua playlist!')
                found_music = True
                break
                
        return found_music

    def busca_banda(self, banda, lista):

        '''
        Busca se a banda se encontra na lista atual. Recebe uma string e a lista a ser comparada.
        Retorna um boolean.
        '''

        found_band = False

        for index in range(len(lista)):
            if (lista[index][0]).lower() == banda.lower():
                found_band = True
                break

        return (found_band, index)
    
    def adiciona_musica(self, musica, banda, lista):

        '''
        Adiciona dois novos elementos a lista de música (música e banda). Retorna a lista atualizada.
        '''
        nova_lista = lista.extend(((banda, musica),))
        return nova_lista

    def main(self, banda, musica):
        
        '''
        Recebe duas strings, a primeira se refere ao nome da banda e a segunda referente a musica.
        Retorna uma mensagem no interpretador. Se a música foi encontrada, ou se encontrou a banda,
        ou se não achou nenhum dos dois ele adiciona a banda e musica na biblioteca de musicas.
        '''

        musicas_contidas = [('Limp Bizkit', 'Break Stuff'),
        ('System of a Down', 'Chop Suey'),
        ('Slipknot', 'Duality')
        ]

        encontrou_musica = self.busca_musica(self, musica, musicas_contidas)
        encontrou_banda = self.busca_banda(self, banda, musicas_contidas)
        

        if encontrou_musica:
            print('Bom proveito')

        elif encontrou_banda[0]:

            print(f'Não encontrei a sua musica, mas exite musica dessa banda: {musicas_contidas[encontrou_banda[1]]}.')
            print('Esta é nossa recomendação.')

        else:
            self.adiciona_musica(self, musica, banda, musicas_contidas)
            print(F'Como não temos essa musica, vou adicionar aqui no nosso banco de dados. Ele está assim hoje:\n\n {musicas_contidas}  ')

a = Lista_de_Musicas
a.main(a, 'Banda_teste', 'Musica_teste')
