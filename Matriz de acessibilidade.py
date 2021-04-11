# Algoritmo Desenvolvido pelo Professor Douglas Maioli

from copy import deepcopy

print('Calculadora da Matriz de Acessibilidade')
print('Desenvolvida pelo Professor Douglas Maioli')
print('-'*30)

A=list()
Ai=list()
R=list()
temp=list()

n=int(input('Quantos vértices tem o grafo?'))
for l in range(0,n):
    for c in range(0,n):
        temp.append(int(input('Digite o elemento da matriz de adjacências na linha {} e coluna {}: '.format(l+1,c+1))))
    A.append(temp[:])
    temp.clear()
    
print('-' *30)
print('A Matriz A^1 é:')
for l in range(0,n):
    print(A[l])

Ai = deepcopy(A)
R = deepcopy(A)

for i in range (2,n+1):
    print('-' * 30)
    print('A Matriz A^{} é:'.format(i))
    for l in range (0,n):
        for c in range (0,n):
            s=0
            for j in range (0,n):
                s += Ai[l][j]*A[j][c]
            if s>=1:
                s=1
                R[l][c]=1
            temp.append(s)
        Ai[l]=(temp[:])
        print(Ai[l])
        temp.clear()
        
print('-' * 30)
print('-' * 30)
print('A Matriz de Acessibilidade R é:')
for l in range (0,n):
    print(R[l])
