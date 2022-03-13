import os
import time

def cria_arvore():

    '''
    Cria uma árvore de Natal. O formato de saída é de uma lista.
    '''

    arvore =[]
    conta = 1
    largura = 20

    for index in range(10):
        arvore.append(("*"*conta).center(largura))
        conta += 2

    return arvore

def imprime_lista(lista):

  '''
  Imprime uma lista linha por linha
  '''
  
  for i in range(len(lista)):
    print(lista[i])

def limpa_a_tela():

  '''
  Limpa a tela para uma nova impressão
  '''

  clear = lambda: os.system('cls')
  clear()

def faz_arvore_piscar(arvore_list):

  tree = arvore_list
  largura = len(tree)
  nova_arvore = []

  for i in range(largura):
    if i >= 2:
        linha = list(tree[i])
        alterar_frente, alterar_tras  = int(largura/2 + (int(i/2))), int(largura/2 - (int(i/2)))
        linha[alterar_frente], linha[alterar_tras] = ' ', ' '
        nova_arvore.append(''.join(linha))

    else:
        nova_arvore.append(tree[i])

  return nova_arvore
  
def main():
    
  '''
  Imprime ima árvore de natal no console de forma que aparenta estar piscado.
  '''

  tree = cria_arvore()
  count = 0
  
  while count < 5:

    imprime_lista(tree)
    print(" |    | ".center(20))
    time.sleep(2)
    limpa_a_tela()
    imprime_lista(faz_arvore_piscar(tree))
    print(" |    | ".center(20))
    time.sleep(2)
    limpa_a_tela()
    count+=1

main()
