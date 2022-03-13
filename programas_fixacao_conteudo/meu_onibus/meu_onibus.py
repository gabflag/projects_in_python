from datetime import timedelta
import re, time


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

  if len(os_possiveis) == 0:
    return 0
  else:
    return len(diferenca) - len(os_possiveis)

  
def cria_lista(string):
  
  '''
  Imprime uma lista com strings contendo apenas 5 caracteres. OBS: Função feita para fase
  de coleta de informação no site da empresa de onibus
  '''

  exemplo = string
  a = list(exemplo)
  lista = []
  laco = True

  while laco:
    lista.append(''.join(a[:5]))
    del(a[:5])
    if len(a) == 0:
      laco = False
  
  print(lista)  

def main():
  
  '''
  Executa o bloco de código e imprime no console o próximo onibus que irá sair.
  Para adicionar ou remover horarios basta criar uma lista com os horarios de saída e o bairro e posterior centro,
  adicionar ambos na lista "group_onb", e adicionar a frase de saída na lista "group_onb_aws". OBS: necessário estarem
  na mesma ordem.
  '''
  
  print('\nBem vindo ao programa de horário de onibus')
  hora_atual, minuto_atual  = int(input('\nDigite a hora que está no ponto: ')), int(input('Digite agora os minutos(formato "02"): '))
  hora_formatada = timedelta(hours= hora_atual, minutes= minuto_atual)
  print('\n')
  
  bairro_um = ['05:05', '05:20']
  centro_um = ['06:55', '07:40']
  
  bairro_dois = ['05:05', '05:20']
  centro_dois = ['06:55', '07:40']

  group_onb = [bairro_um, centro_um,
  bairro_dois, centro_dois
  ]
  
  group_onb_aws = ['O próximo BAIRRO_01 saída bairro: ', 'O próxímo BAIRRO_01 saída centro: ',
  'O próximo BAIRRO_02 saída bairro: ', 'O próxímo BAIRRO_02 saída centro: '
  ]

  for i in range(len(group_onb)):
    index = retorna_proximo(group_onb[i], hora_formatada)
    horario_do_onibus = group_onb[i][index]
    print(f'{group_onb_aws[i]} {horario_do_onibus}')

    if (i % 2) != 0:
      print("\n")

  time.sleep(120)

main()
