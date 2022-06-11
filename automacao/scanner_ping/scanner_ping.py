import os

def scan():
	os.system('clear')
	ip = input('IP que representa a rede (192.168.6.0): ').split('.')
	h_inicial = int(input('Host inicial: '))
	h_final = int(input('Host final: '))

	disponivel = []
	ocupado = []

	for i in range(h_inicial,(h_final+1)):
		
		ip[3] = str(i)
		ip_formatado = '.'.join(ip)
		print ('\nTesting...')
		rs = os.system('ping -c 1 {}'.format(ip_formatado))

		if rs == 0:
			ocupado.append(ip_formatado)
		else:
			disponivel.append(ip_formatado)
	
	os.system('clear')

	mantem_laco = 0
	while(mantem_laco == 0):	
	
		opcao = int(input("\n\nMostrar lista de disponiveis digitar um (1) ou dois(2) para a de indisponiveis: "))

		if (opcao == 1):
			print("\n\n############################")
			print("Lista de IP's disponiveis\n\n")
			for i in range(len(disponivel)):
				print(disponivel[i])

		if (opcao == 2):	
			print("\n\n############################")
			print("Lista de IP's indisponiveis\n")
			for i in range(len(ocupado)):
				print(ocupado[i])
		
		mantem_laco=int(input("Imprimir novamente umas das opcoes? 1 (SIM) ou 2 (NAO)"))

def main():
	mantem_laco = 1
	while(mantem_laco == 1):
		scan()
		mantem_laco=int(input("Digite um (1) para encerrar ou dois(2) para um novo scanner de rede: "))

main()

