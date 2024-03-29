import random
import matplotlib.pyplot as plt
import numpy as np

valoresFuncaoHeuristicaPrimeiraEscolha = []
valoresFuncaoHeuristicaMelhorEscolha = []

def tabuleiro(n, q):
	tabuleiros = []
	for q in range(q):
		tabuleiro = []
		for i in range(n):
			tabuleiro.append(random.randint(1, n))
		tabuleiros.append(tabuleiro)
	return tabuleiros

def todosVizinhos(tabuleiro):
	vizinhos = []
	for k in range(0,len(tabuleiro)):
		novoTabuleiro = tabuleiro.copy()
		temp = tabuleiro[k]
		j = 1
		while(j <= len(tabuleiro)):
			if(j == temp):
				j +=1
				continue
			novoTabuleiro[k] = j
			vizinhos.append(novoTabuleiro.copy())
			j += 1
	return vizinhos

def umVizinho(tabuleiro):
	vizinhos = todosVizinhos(tabuleiro)
	sorteado = random.sample(vizinhos, 1)
	escolhido = sorteado[0]
	return escolhido

def numeroAtaques(node):
	conflict = []
	for i in range(0,len(node)):
		for j in range(0,len(node)):
			if (i == j):
				continue
			if (node[i] == node[j]):
				if ([i, j] in conflict or [j, i] in conflict):
					continue
				conflict.append([i, j])
				continue
			if (node[i] != node[j]):
				d = abs(i-j)
				if (node[i] == node[j] + d or node[i] == node[j] - d):
					if ([i, j] in conflict or [j, i] in conflict):
						continue
					conflict.append([i, j])
					continue
	c = len(conflict)
	return c

def hillClimbingPrimeiraEscolha(tabuleiro):
	tc = tabuleiro.copy()
	tamanhoTabuleiro = len(tabuleiro)
	tamanhoMaximo = (tamanhoTabuleiro**2 - tamanhoTabuleiro)
	lista = []
	numAtaqtc = numeroAtaques(tc)
	while True:
		ts = umVizinho(tc)
		numAtaqts = numeroAtaques(ts)
		if(len(lista) == tamanhoMaximo):
			par = [tc, numAtaqtc]
			valoresFuncaoHeuristicaPrimeiraEscolha.append(numAtaqtc)
			return par
		if ts in lista:
			continue
		if numAtaqts >= numAtaqtc:
			lista.append(ts)
		if numAtaqts < numAtaqtc:
			valoresFuncaoHeuristicaPrimeiraEscolha.append(numAtaqtc)
			return hillClimbingPrimeiraEscolha(ts)
	
	

def hillClimbingMelhorEscolha(tabuleiro):
	tc = tabuleiro.copy()
	vizinhos = todosVizinhos(tc)
	avaliação = []
	minvizinhos = []
	numAtaqtc = numeroAtaques(tc)
	for i in vizinhos:
		avaliação.append([i,numeroAtaques(i)])
	low = numeroAtaques(tc)
	for i in avaliação:
		temp = i[1]
		if temp < low:
			low = temp
	if low == numeroAtaques(tc):
		par = [tc, numAtaqtc]
		valoresFuncaoHeuristicaMelhorEscolha.append(numAtaqtc)
		return par
	for i in avaliação:
		if i[1] == low:
			minvizinhos.append(i[0])
	sorteado = random.sample(minvizinhos, 1)
	escolhido = sorteado[0]
	valoresFuncaoHeuristicaMelhorEscolha.append(numAtaqtc)
	return hillClimbingMelhorEscolha(escolhido)

	
def mainPrimeiraEscolha(n,q):
	EstadosFinais = []
	tabuleiros = tabuleiro(n, q)
	for i in tabuleiros:
		temp = hillClimbingPrimeiraEscolha(i)
		EstadosFinais.append(temp)
	return EstadosFinais


def mainMelhorEscolha(n,q):
	EstadosFinais = []
	tabuleiros = tabuleiro(n, q)
	for i in tabuleiros:
		temp = hillClimbingMelhorEscolha(i)
		EstadosFinais.append(temp)
	return EstadosFinais

def analise(tamanhoTabuleiro, numerosimulações):
	valoresFuncaoHeuristicaPrimeiraEscolha.clear() 
	valoresFuncaoHeuristicaMelhorEscolha.clear()
	EstadosFinaisPrimeiraEscolha = mainPrimeiraEscolha(tamanhoTabuleiro,numerosimulações)
	EstadosFinaisMelhorEscolha= mainMelhorEscolha(tamanhoTabuleiro,numerosimulações)
	sum = 0
	for n in range(1,tamanhoTabuleiro):
		sum += n
	x1 = []
	x2 = []
	for i in range(len(valoresFuncaoHeuristicaPrimeiraEscolha)):
		x1.append(i+1)
	for i in range(len(valoresFuncaoHeuristicaMelhorEscolha)):
		x2.append(i+1)
	
	y1 = valoresFuncaoHeuristicaPrimeiraEscolha
	y2 = valoresFuncaoHeuristicaMelhorEscolha

	# plotting the points
	plt.grid(True)
	plt.plot(x1, y1)
	plt.plot(x2, y2)
	# naming the x axis
	plt.xlabel('Numero de estados até chegar ao final')
	# naming the y axis
	plt.ylabel('Numero de ataques')

	# giving a title to my graph
	plt.title('Grafico de desempenho comparando primeira e melhor escolha')

	# function to show the plot
	plt.show()


analise(4,1)
analise(8,1)
analise(16,1)
analise(32,1)