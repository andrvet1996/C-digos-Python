#PRIMEIROS COMANDOS

#DESAFIO 1
#nome = input ('Qual é o seu nome?')
#print ("Olá",nome,'!','Prazer em te conhecer!')

#DESAFIO 2
#dia = input ('Em que dia você nasceu?')
#mês = input ('Em que mês você nasceu (escreva o mês)?')
#ano = input ('Em que ano você nasceu?')
#print ('Você nasceu no dia', dia, "do", mês, 'de', ano,'. Correto?')

#DESAFIO 3
#n1 = eval (input ('Digite o primeiro número:'))
#n2 = eval (input ('Digite o segundo número:'))
#soma = n1 + n2
#print ('A soma é', soma,'.')

#EXERCÍCIO 2 (parece o desafio 1)
#nome = input ('Digite seu nome: ')
#print ('É um prazer te conhecer, {}!'.format(nome)) 


#TIPOS PRIMITIVOS (int, float, bool=True or False, str)
#Exemplo 1
#n1 = int (input ('Digite o primeiro número:'))
#n2 = int (input ('Digite o segundo número:'))
#s = n1+n2
#print ('A soma entre', n1, 'e', n2, 'vale', s) 

#Desafio 2 is. alguma coisa
#n = input ('Digite algo:')
#print (n.isnumeric()) #confira se é inteiro
#print (n.isalpha())#confirma se é letra
#print (n.isalnum())#confirma se é letra e número 3a por exemplo
#print (n.isupper())

#Desafio 3 soma de números e apresentar resultado
n1 = int (input ('Digite o primeiro número: '))
n2 = int (input ('Digite o segundo número:  '))
n3 = int (input ('Digite o terceiro número: '))
s = n1+n2+n3
print ('A soma de {}, {} e {} é {}'. format (n1, n2, n3, s))

#EXERCÍCIO 4 dissecando uma variável
#a = input ('Digite algo: ')
#print ('O tipo primitivo desse valor é', type(a))
#print ('Só possui espaço?', a.isspace())
#print ('É um número?', a.isnumeric())
#print ('É alfabético?', a.isalpha())
#print ('É alfanumérico?', a.isalnum())
#print ('Está em maiúscula?', a.isupper())
#print ('Está em minúscula?', a.islower())
#print ('Está capitalizada?', a.istitle())#só primeira letra maiúscula

#Outra forma de fazer
a = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(a)}')
print(f'Só há espaços? {a.isspace()}')
print(f'É um número? {a.isnumeric()}')
print(f'É alfabético? {a.isalpha()}')
print(f'É alfanumérico? {a.isalnum()}')
print(f'Todas as letras são maiúsculas? {a.isupper()}')
print(f'Todas as letras são minúsculas? {a.islower()}')
print(f'Está capitalizada? {a.istitle()}')

#OPERADORES ARITMÉTICOS
#a = 2**3
#a = pow (2,3) isso é igual a 2**3
#print (a)

#raiz quadrada
#a = 25**(1/2)
#print (a)

#raiz cúbica
#a = 27**(1/3)
#print (a)

#nome = input ('Qual é o seu nome? ')
#print ('Prazer em conhecê-lo {:=^20}!'.format(nome))
# {:20} em 20 espaços 
# {:>20} em 20 espaços a direita
# {:<20} em 20 espaços a esquerda
# {:^20} em 20 espaços centralizado
# {:=^20} em 20 espaços centralizado com símbolo = ou outro que vc escolher

#n1 = int (input ('Digite o primeiro número: '))
#n2 = int (input ('Digite o segundo número: '))
#s = n1 + n2
#m = n1 * n2
#d = n1 / n2
#di = n1 // n2
#e = n1 ** n2

#print ('A soma é {}, o produto é {} e a divisão é {}.'. format (s, m, d), end=' ')
#end='' comando para não quebrar linha nos print
#print ('A soma é {}, o produto é {} e a divisão é {:.2f}.'. format (s, m, d))
#na divisão vai aparecer duas casas decimais
#print ('A divisão inteira é {} e a potência é {}.'. format (di, e))

#Desafio 5 sucessor e antecessor
n = int (input ('Escolha um número inteiro: '))
n1 = n - 1
n2 = n + 1
print ('O seu antecessor é {} e o sucessor é {}.'.format (n1, n2))
#print ('A soma entre {} e {} vale {}'.format(n1, n2, s))#outra forma

#outra forma de fazer, sem criar variáveis
n = int (input('Digite um número: '))
print ('Analisando o valor {}, seu antecessor é {} e o sucessor é {}.'.format (n, (n-1), (n+1)))

#Desafio 6 
#n = int (input ('Digite um número: '))
#dn = n * 2
#tn = n * 3
#rqn = n ** (1/2)
#print ('O dobro do número, o triplo e a raiz quadrada são, respectivamente {}, {} e {}.'.format (dn, tn, rqn))

#Desafio 7
#n1 = int (input ('Nota 1: '))
#n2 = int (input ('Nota 2: '))
#M = (n1 + n2) / 2
#print ('A média do aluno é {}.'. format (M))

#Desafio 8

m = int (input ('Digite o valor em metros: ')) 
cm = m * 100
mm = cm * 10
print ('O valor em centrímetros e milímetros são, respectivamente, {}cm e {}mm.'. format (cm, mm))

#Desafio 9 tabuada
n = int (input ('Digite um número: '))
n1 = n * 1
n2 = n * 2
n3 = n * 3
n4 = n * 4
n5 = n * 5
n6 = n * 6
n7 = n * 7
n8 = n * 8
n9 = n * 9
n10 = n * 10
print ('A tabuada no número digitado e: {},{},{},{},{},{},{},{},{},{}.'
.format (n1,n2,n3,n4,n5,n6,n7,n8,n9,n10))

#outra forma, sem criar vriáveis
n = int (input ('Digite um número para ver sua tabuada: '))
print ('*' * 12)
print ('{} * {:2} = {}'.format (n, 1, n*1))
print ('{} * {:2} = {}'.format (n, 2, n*2))
print ('{} * {:2} = {}'.format (n, 3, n*3))
print ('{} * {:2} = {}'.format (n, 4, n*4))
print ('{} * {:2} = {}'.format (n, 5, n*5))
print ('{} * {:2} = {}'.format (n, 6, n*6))
print ('{} * {:2} = {}'.format (n, 7, n*7))
print ('{} * {:2} = {}'.format (n, 8, n*8))
print ('{} * {:2} = {}'.format (n, 9, n*9))
print ('{} * {:2} = {}'.format (n, 10, n*10))
print ('*' * 12)

#Desafio 10 conversão real/dólar
r = eval (input('Quantos reais você possui? R$ '))
d = r / 3.27
print ('A sua quantia reais corresponde a {:.2f} dólares.'. format (d))

#Desafio 11 área para pintar
l = eval (input ('Qual a largura em metros? '))
h = eval (input ('Qual a altura em metros? ')) 
a = l * h
qt = a / 2
print ('Sua parede possui a área de {:.1f} metros quadrados.'.format (a))
print ('A quantidade de tinta utilizada será de {:.1f} litros.'.format (qt))

#Desafio 12 desconto
p = eval (input ('Digite o preço atual: R$ '))
npcd = p - (p * 0.05)
print ('O preço com desconto de 5% é R${:.2f}.'.format (npcd))

#Desafio 13 reajuste salarial
s = eval (input ('Digite seu salário atual: '))
ns = s + (s * 0.15)
print ('Seu salário com o aumento de 15% é R$ {:.2f}.'.format (ns))

#Exercício 14-conversão temperatura
c = eval (input('Digite a temperatura em ºC: '))
f = 32 + 1.8 * c
k = c + 273
print ('A temperatura {}ºC corresponde a {:.1f}ºF e {:.1f}K.'.format (c, f, k))

#Exercício 15-custo aluguel de carro
d = eval (input ('Quantos dias você ficou com o carro? '))
q = eval (input('Quantos quilometros você percorreu? '))
p = (60 * d) + (0.15 * q)
print ('O total a pagar é R${:.2f}.'.format (p))


#Aula 8- comandos math e random
#import math #impora tudo
#n = eval (input ('Digite um número: '))
#raiz = math.sqrt (n)
#print ('A raiz quadrada de {} é {:.3f}.'.format (n, raiz))

#from math import sqrt
#n = eval (input ('Digite um número: '))
#raiz = sqrt(n)
#print ('A raiz quadrada de {} é {:.2f}.'.format (n, raiz))

#import random  # gera número aleatório
#n = random.random()
#print(n)

#import random
#n = random.randint (1,10)#randint gera aleatórios dentro de um intervalo
#print(n)

import emoji   #importar emoji                                                    
print(emoji.emojize('Olá, mundo: sunglasses:', use_aliases=True))  

