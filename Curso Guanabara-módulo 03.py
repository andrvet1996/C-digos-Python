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
