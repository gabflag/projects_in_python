
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

  part_bairro_jose_nt = ['05:45', '06:00', '06:35', '06:45', '07:00', '07:40', '08:35', '09:45', '11:10', '12:05', '13:10', '14:00', '15:20', '16:40', '17:50', '19:15', '22:35']
  part_centro_jose_nt = ['06:15', '06:20', '07:00', '07:55', '09:10', '10:30', '11:25', '12:30', '13:20', '14:40', '16:00', '17:10', '18:25', '19:40', '21:00', '22:00', '23:30']
  hr_simples = ["12:50", "15:30", "19:45"]

  index = retorna_proximo(part_centro_jose_nt  , hora_formatada)

  print(part_centro_jose_nt[index])


main()
