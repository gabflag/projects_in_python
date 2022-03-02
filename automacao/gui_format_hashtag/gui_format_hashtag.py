from tkinter import *
import re

class hashtag:

    def __init__(self):
        self.window = Tk()
        self.window.title("Format your hashtag")
        self.window.geometry("1350x500+0+0") #largura - altura - distância da borda esqueda - diantancia do fundo

        self.entrada = Text(self.window)
        self.entrada.insert(INSERT, "Cole aqui o texto a ser formatado!")
        self.entrada.grid(column=0, row=4)

        self.saida = Text(self.window)
        self.saida.insert(INSERT, 'Resultado')
        self.saida.grid(column=3, row=4)

        self.botao = Button(self.window, text="Fazer formatação", command=self.main)
        self.botao.grid(column=2, row=1)

        self.espaco_02 = Label(self.window, text="").grid(column=2, row=2)

        self.window.mainloop()

    def remove_special_characters(self, text):

        '''
        Remove caracteres indesejados de uma string inteira. Retorna uma string com esse tratamento.
        '''
        
        caracter_esp = '.!?,@%$\n '
        nova_string = "".join([ caracter for caracter in text if caracter not in caracter_esp])
        return nova_string

    def remove_repeated(self, text_in_list):
        
        '''
        Remove palavras repitidas dentro da lista. Retorna uma lista com esse tratamento.
        '''
        
        new_text_in_list = []
        for index in range(len(text_in_list)):
            hashtag = (text_in_list[index]).lower()
            if  hashtag not in new_text_in_list and hashtag != '':
                new_text_in_list.append(hashtag)

        return new_text_in_list

    def main(self):

        '''
        Recebe uma string e faz o tratamento. Retira espaçamentos desnecessários, palavras repitidas, deixa tudo em minusculo
        e adiciona 3 pontos ao inicio das hastags. Retorna o texto tratado.
        '''
        
        text = self.entrada.get(1.0, END)
        text_ok = self.remove_repeated(re.split(r'[#]', self.remove_special_characters(text)))
        size_text = len(text_ok)
        new_string = '.\n.\n.\n\n'
        for index in range(size_text):
            new_string+= ('#' + text_ok[index]) + ' '
            
        self.saida.delete(1.0,END)
        self.saida.insert(INSERT,new_string)

test = hashtag()
