#!/usr/bin/env python

class Resolve():
	
	# inicializa
	def __init__(self):
		# regra adjacencia
		self.adjacencia = [(-1,-1),(-1, 0),(-1, 1),(0, -1),(0, 1),(1, -1),(1, 0),(1, 1)]
		# entrada quantidade linha
		try:
			self.N = int(raw_input())
		except ValueError as err:
			print err
		# entrada quandidade coluna
		try:
			self.M = int(raw_input())
		except ValueError as err:
			print err
		self.matriz = []
		# armazena entrada matriz
		for i in range(self.N):
			# forca int para cada posicao da matriz, separando os elementos por espaco
			self.matriz.append(map(int, raw_input().split()))
		self.visitado = []

	# monta matriz tamanho NxM com -1 para marcacao
	def montaVisitado(self):
		visitado = []
		for i in range(self.N):
			v = []
			for j in range(self.M):
				v.append(int(-1))
			visitado.append(v)
		self.visitado = visitado
		
	# busca em profundidade, recursivo
	def prof(self, i, j, mat, visit, c):
		# nao estoura tamanho matriz
		if i < 0 or i >= len(mat) or j < 0 or j >= len(mat[0]):
			return
		# pular se 'vazio'
		if mat[i][j] == 0:
			return
		# pular se ja visitou
		if visit[i][j] != -1:
			return
		# marca visitado com o numero da primeira posicao do conjunto adjacente
		visit[i][j] = c
		# verifica se ha adjacencia
		for d in self.adjacencia:
			self.prof(i+d[0], j+d[1], mat, visit, c)

	# percorre a matriz para resolver
	def resolve(self):
		self.montaVisitado()
		# marcador de posicao
		c = 0
		for i in range(self.N):
			for j in range(self.M):
				self.prof(i, j, self.matriz, self.visitado, c)
				c = c + 1
		# gera vetor zerado para contar elementos conectados qte elementos NxM
		conta = [0]*(self.N *self.M)
		for i in range(self.N):
			for j in range(self.M):
				if self.visitado[i][j] != -1:
					# incrementa no primeiro elemento do conjunto adjacente
					conta[self.visitado[i][j]] = conta[self.visitado[i][j]] + 1
		return max(conta)
	
# instancia a classe
if __name__ == '__main__':
	solucao = Resolve()
	print solucao.resolve()
