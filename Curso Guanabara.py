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



#print ('A soma entre {} e {} vale {}'.format(n1, n2, s))#outra forma


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
