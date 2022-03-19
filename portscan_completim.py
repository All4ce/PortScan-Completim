# Criando um PortScan mais completo com o conhecimento que adquiri.
import socket
import sys
import portscan_list

def portscan():

	if(len(sys.argv) <=1):
		print("[*] Informe o IP no argumento >>> ./portscan_completim.py IP/SITE")
	elif(len(sys.argv) > 2):
		print("[*] So aceitamos 1 argumento")
	else:
		ip = sys.argv[1]
		c = False
		portas = portscan_list.escolhendo_lista()
		print(f"[*] Varrendo portas no host: {ip}")

		for i in portas: #Criando o socket pra conexao e validando portas
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			socket.setdefaulttimeout(0.5) # Pra nao demorar muito! 

			if (sock.connect_ex((ip,i)) == 0):
				c = True
				print (f"[$] Porta TCP Aberta: {i}")
				sock.close() # Boas praticas em dia!
		if(c == False):
			print("[*] Nenhuma porta esta aberta!")
portscan()
