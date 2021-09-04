#Aula 16-TUPLAS símbolo ()
#AS TUPLAS SÃO IMUTAVEIS#

'''lanche = ('hambúrger','suco','pizza','pudim') #pode ser sem parênteses
print(lanche)
print(lanche[1])
print(lanche[-4])
print(lanche[1:3])#retira o elemento 3
print(lanche[2:])
print(lanche[:2])#mostra o elemento 0 e 1 e retira o 2

for comida in lanche:
    print ('Eu vou comer {}.'.format(comida))#print(f'Eu vou comer {comida}'')
print('Comi pra caramba!')

for cont in range (0, len(lanche)):
    print (lanche[cont])#se colocar só o cont imprimi os números
print('Comi pra caramba!')

#PARA MOSTRAR A POSIÇÃO

for pos, comida in enumerate (lanche):
    print ('Eu vou comer {} na posição {}.'.format(comida, pos))
    
lanche = ('hambúrger','suco','pizza','pudim')
print (sorted(lanche)) # ordena a tupla'''
    
a = (2,5,4)
b = (5,8,1,2)
c = (a + b)
print(c)
print(len(c))#conta o numero de elementos
print(c.count(5))#quantas x aparece 5 na tupla c
print(c.index(8))#mostra a posiçao do elemento

#del (c) esse comando apaga a tupla toda


#Desafio 72-número por extenso
cont = ('zero', 'um','dois','três','quatro',
'cinco', 'seis','sete','oito','nove',
'dez','onze','doze','treze','catorze',
'quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

while True:
    núm = int(input('Digite um número entre 0 e 20: '))
    if 0 <= núm <= 20:
        break
    print ('Tente novamente.', end= '')#end = '' não pular linha
    
print ('Você digitou o número {}.'.format (cont[núm]))
#print (f'Você digitou o número {cont[núm]})


#Desafio 73-Tuplas com times
times = ('Atlético-MG','Palmeiras','Fortaleza','RB Bragantino','Flamengo','Athletico-PR',	
'Ceará','Santos','Atlético-GO','Bahia','Internacional','Corinthians','Fluminense',
'Juventude','Sport','São Paulo','América-MG','Cuiabá','Grêmio','Chapecoense')

print('=-='*39)
print ('Lista de times do Brasileirão: {}.'.format(times))
print('=-='*39)
 
print ('Os 5 primeiros colocados são: {}.'.format(times[0:5]))
print ('=-='*20)
print ('Os últimos 4 colocados são: {}.'.format(times[16:20]))# ou [-4:0]
print ('=-='*20)
print ('Os times em orde alfabética são: {}.'.format(sorted(times)))
print ('=-='*11)
print ('O Chapecoense está na {}ª posição.'. format(times.index('Chapecoense') + 1))#index para encontrar um termo + 1 posiçao real
#print(f'O Chapecoense está na {times.index("Chapecoense")+ 1}ª posição')
print ('=-='*11)


#Desafio 74-maior e menor número em tuplas
from random import randint
sorteados = (randint(1,10), randint(1,10), randint(1,10),randint(1,10), randint(1,10))#gera tupla
print ('Os valores sorteados foram: ', end = '')
for n in sorteados:#imprimi os valor fora da tupla
    print ('{} '.format (n), end = '')
    
print ('\nO maior valor sorteado foi {}.'.format (max(sorteados)))#max método para tupla \n pula linha
print ('O menor valor sorteado foi {}.'.format (min(sorteados)))


#Desafio 75-análise de tupla
núm = (int(input('Digite um número: ')), 
int(input('Digite outro número: ')),
int (input('Digite mais um número: ')),
int (input ('Digite o último número: ')))

print ('Você digitou os números {}.'.format (núm))
print ('O valor 9 apareceu {} vezes.'.format (núm.count (9)))
if 3 in núm:
    print ('O valor 3 apareceu na {}ª posição.'.format (núm.index(3) + 1))
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print ('Os valores pares digitados foram ' , end = '')
for n in núm:
    if n % 2 == 0:
        print (n, end = '')
        
        
#Exercício 76-lista de preços com tuplas
print('=' * 40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))  # comando para centralizar
print('=' * 40)

listagem = ('Lápis', '1.75',
            'Borracha', '2.00',
            'Caderno', '15.90',
            'Estojo', '25.00',
            'Transferidor', '4.20',
            'Compasso', '9.99',
            'Mochila', '120.32',
            'Canetas', '22.30',
            'Livro', '34.90')
for posição in range (0, len(listagem)):
    if posição % 2 == 0: #observe que os produtos estão na posição par
        print(f'{listagem[posição]:.<30}', end='')#alinhado a esquerda com pontos não pular linha com o preço
    else:
        print(f'R${listagem[posição]:>7}')
print('=' * 40)

#Desafio 77-contar vogal na tupla
palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM'
'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 
'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for p in palavras:
    print ('\nNa palavra {} temos '.format (p), end = '')
    for letra in p:
        if letra.upper() in 'AEIOU':
            print (letra, end = '')
            
            
AULA 17-LISTAS

#num = (2,5,9,1)#tupla
#num [2] = 3
#print (num)

#num = [2,9,5,1,9]
#num [2] = 0#mudou o elemento da posição 2
#num.append (7)#estou adicionando o valor 100
#num.sort ()#ordena
#num.sort (reverse=True)#ordena reverso
#print(num)
#num.insert (2,1000)#inseri o valor 1000 na posição 2
#num.pop()#deleta o último valor
#num.remove (9)#remove um valor numérico em sua primeira ocorrência
#if 100 in num:#consulta se o número está na lista
    num.remove (100)
else:
     print ('O número não existe na lista.')
    
#print (num)
print ('Essa lista tem {} elementos.'.format(len (num)))
#print (f'Essa lista tem {len(num)} elementos.')

#valores = list()
#valores.append (1)
#valores.append (1000)
#valores.append (3)

#for v in valores:
    #print (f' {} ...', end = '')#não pula linha
    #print ('{} ...'.format(v), end = '')
    
#for c, v in enumerate (valores):
    #print ('Na posição {} encontrei o valor {}.'.format (c,v))
#print ('Cheguei ao final da lista.')

#valores = list()
#for cont in range (0, 5):#incluir valores na lista
    #valores.append (int(input('Digite um valor: ')))
#print ('A lista de números é: {}.'.format (valores))

a = [1, 23, 12, 100]
#b = a # as duas listas estão ligadas
b = a[:] #b recebe todos os elementos de a, isso é uma COPIA
b [2] = 8
print ('Lista A: {}.'.format(a))
print ('Lista B: {}.'.format (b))


#Desafio 78-maior e menor valor em lista
listnum = []
maior = 0
menor = 0
for c in range(0, 5):
    listnum.append(int(input('Digite um valor para a posição {}: '.format(c)))),
    if c == 0:
        maior = menor = listnum[c]#vc digitou um número somente ele é o maior e o menor
    else:
        if listnum[c] > maior:
            maior = listnum[c]
        if listnum[c] < menor:
            menor = listnum[c]

print('=-' * 30)
print(f'Você digitou os valores {listnum}')
print(f'O maior valor foi {maior}, nas posições .', end='')
for i, v in enumerate(listnum):
    if v == maior:
        print(f'{i}...', end='')
print ()
print(f'O menor valor foi {menor}, nas posições .', end='')
for i, v in enumerate(listnum):
    if v == menor:
        print(f'{i}...', end='')
print()


# Desafio 79-valores únicos em uma lista

números = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('Adicionado com sucesso!')
    else:
        print('Valor duplicado! Não será adicionado.')

    resposta = str(input('Quer continuar? [S/N]: ')).upper().strip()
    if resposta in 'N':
        break
    print('Digite novamente sua opção')
print('=-' * 30)
números.sort()
print('Você digitou os valores {}.'.format(números))
print('=-' * 30)


#Desafio 81-Extraindo dados de uma lista
lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    resposta = str(input('Quer continuar?[S/N]: ')).upper().strip()
    if resposta in 'N':
        break
print('=-' * 30)
print('Você digitou {} números.'.format(len(lista)))
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}.')
if 5 in lista:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte da lista.')
