# Lista de portas mais utilizadas

print("[*] ==== All4ce Sec // PortScan ==== [*]")
print("[*] Escolha qual das 3 listas deseja realizar um PortScan! ")

def escolhendo_lista():
	lista_1 = [21,22,23,25,80,110,139,443,445,3389]
	lista_2 = [135,139,143,443,445,993,995,1723,3306,3389,5900,8080]
	lista_3 = [3390,5060,5666,5900,6001,8000,8008,8080,8443,8888,10000,32768,49152,49154]
	lista = []

	print (f"[*] 1 >>> {lista_1} \n[*] 2 >>> {lista_2} \n[*] 3 >>> {lista_3} \n")

	lista_escolhida = input("[*] >>> ")

	if (lista_escolhida == '1'):
	 	lista = lista_1
	 	return lista
	elif (lista_escolhida == '2'):
	 	lista = lista_2
	 	return lista
	elif (lista_escolhida == '3'):
	 	lista = lista_3
	 	return lista
	else:
		print("[*] Opcao nao encontrata, tente novamente")