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
