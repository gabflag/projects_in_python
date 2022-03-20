from tkinter import *
import string, secrets

class Gerador_de_senha:
    
    '''
    Cria uma GUI e nela pode-se gerar uma senha. Basta especificar a quantidade de caracteres
    e clicar uma vez no botão 'DO', as senha irá aparecer no campo de texto abaixo.
    '''

    def __init__(self):

        self.window = Tk()
        self.window.title("Make here your new password")
        self.window.geometry("600x600+0+0") #largura - altura - distância da borda esqueda - diantancia do fundo

        self.label = Label(self.window, text="Make a new password:").grid(column=1, row=0)

        self.botao = Button(self.window, text="DO", command=self.main)
        self.botao.grid(column=1, row=1)

        self.espaco = Label(self.window, text="").grid(column=1, row=2)
        self.label_02 = Label(self.window, text="Number of characters").grid(column=1, row=3)

        self.entrada = Entry(self.window)
        self.entrada.insert(INSERT, "20")
        self.entrada.grid(column=1, row=4)
        
        self.espaco_02 = Label(self.window, text="").grid(column=1, row=5)

        self.resultado = Text(self.window)
        self.resultado.insert(INSERT, 'Result')
        self.resultado.grid(column=1, row=6)

        self.window.mainloop()

    def main(self,):

        '''
        Recebe um int na entrada e retorna uma senha forte com 
        numero tota de caracteres iguais ao int da entrada.
        '''

        number_char = int(self.entrada.get())

        caractere_senha = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        password = ''

        for x in range(number_char):
            letra = secrets.choice(caractere_senha)
            password += letra

        self.resultado.delete(1.0,END)
        self.resultado.insert(INSERT,password)

teste = Gerador_de_senha() 
