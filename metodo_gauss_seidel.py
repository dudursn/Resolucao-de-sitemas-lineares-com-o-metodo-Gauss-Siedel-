# -*- coding: utf-8 -*-

'''
Método de Gauss-Siedel para resolução de sistemas lineares
Feita por Eduardo Roger Silva Nascimento
Graduando de Ciência da Computação na Universidade Federal do Maranhão(UFMA)
'''

'''Sistema
    4x + 2y + 1z = 11
    -x + 2y + 0z = 3
    2x +  y + 4z = 16
    Solucao:{1,2,3}
'''
iteracao = int(input("Numero de iterações: "))

# A * x = B
A = [[4,2,1],[-1,2,0],[2,1,4]]
B =	[11,3,16]

#Vetor x inicial na iteração 0
x = [1,1,1]
k = 0

while(k<iteracao):
	for i in range(len(A)):
		soma = 0
		for j in range(i):
			soma = soma +(A[i][j]*x[j])
		for j in range(i+1, len(A)):
			soma = soma +(A[i][j]*x[j])
		x[i] = (1/A[i][i])*(B[i] - soma)
	k+=1
print("Solucao")
print(x)
