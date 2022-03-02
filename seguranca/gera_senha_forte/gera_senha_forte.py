import string, secrets

class Gerador_de_senha:

    def gera_senha(self, qnt_caracteres):

        '''
        Recebe um int na entrada e retorna uma senha forte com 
        numero totaL de caracteres iguais ao int da entrada.
        '''

        caractere_senha = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        password = ''

        for x in range(qnt_caracteres):
            letra = secrets.choice(caractere_senha)
            password += letra
        
        return password

a = Gerador_de_senha
print(a.gera_senha(a, 15))
