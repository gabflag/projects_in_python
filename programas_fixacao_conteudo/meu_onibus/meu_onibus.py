
from datetime import timedelta
import re


def retorna_proximo(lista, hora_formatada):

  '''
  Recebe uma lista de horarios em ordem crescente e o horario principal. Retorna o index
  do elemento da lista de horarios mais proximo da hora principal.
  '''
  
  horario = lista
  teste = hora_formatada

  diferenca = []

  for i in range(len(horario)):
    hm = re.split(":", horario[i])
    teste2 = timedelta(hours= int(hm[0]), minutes= int(hm[1]))
    calculo = teste2 - teste
    diferenca.append(calculo)

  os_possiveis = []
  for i in range(len(diferenca)):
    if diferenca[i] >= timedelta():
      os_possiveis.append(diferenca[i])

  return len(diferenca)- len(os_possiveis)


def main():

  hora_atual = 15
  minuto_atual = 25
  hora_formatada = timedelta(hours= hora_atual, minutes= minuto_atual)
  
main()
