# @uthor: Diego Narducci Arioza
# Versão: 0.1a

import random
import time
import os

rodar = True

lista_full = []

lista_frases = open('lista.txt','r', encoding="utf-8")
lista_frases.seek(0)
lista_frases = lista_frases.read().split('\n')

for i in lista_frases:
	lista_full.append(i.split('='))

len_lista = len(lista_full)

while True:
		
	sorteio = random.choice(lista_full)
	busca_index_sorteado = lista_full.index(sorteio)
	sorteio_n = random.choice(range(1,5))
	print("Perguntas Restantes:", len(lista_full))
	print("Qual é a função do músculo:", sorteio[0], "?")
	print()

	l = []
	alternativas = [1,2,3,4]

	for i in alternativas:
		if i == sorteio_n:
			print(i, "-", sorteio[1])
		else:
			while True:
				sorteio2 = random.choice(lista_full)
				if sorteio2[0] != sorteio[0]:
					print(i, "-", sorteio2[1])
					break

	print()
	resposta = int(input("Qual é a resposta: "))

	if resposta == sorteio_n:
		print("Voce acertou !!!")
		del lista_full[busca_index_sorteado]
	else:
		print("Voce errou !!!")
		print("Resposta Correta é -> ", i, "-", sorteio[1])
		time.sleep(2)
	
	time.sleep(2)
	os.system('clear')

