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
