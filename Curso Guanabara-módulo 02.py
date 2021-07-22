#Aula 12-condições aninhadas
nome = str (input ('Qual é o seu nome: '))
if nome == 'Gustavo':
    print ('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print ('Seu nome é bem popular no Brasil!')
elif nome in ('Ana Cláudia Jéssica Julina'):
    print ('Belo nome feminino!')
else:# se vc tirar o else funciona,mas só printa o último print
    print ('Seu nome é bem normal!')
print ('Tenha um bom dia, {}!'.format (nome)) 

#Desafio 36-número de prestações não pode exceder 30% do salário
v = float (input ('Qual o valor da casa que deseja adquirir? R$'))
s = float (input ('Qual é o seu salário? R$'))
t = int (input ('Em quantos anos de financiamento?' ))
valprest = (v / (t * 12))#parcelas mensais
lim30 = (0.3 * s)
if valprest <= lim30:
    print ('O empréstimo para adquirir uma casa de {:.2f}, a ser pago em {} parcelas mensais, no valor de R$ {:.2f} foi APROVADO!'.format (v, t, valprest))
else:
    print ('O empréstimo NÃO FOI APROVADO, pois o valor da prestação ultrapassa 30% de sua renda mensal.')
    
Dsafio 37- conversor de decimal para binário, octal e hexadecimal    
num = int (input ('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão: 
[1] converter para BINÁRIO 
[2] converter para OCTAL 
[3] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}.'.format (num, bin(num)[2:]))#[2;0] retira algarismos desnecessários
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}.'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}.'.format(num, hex(num)[2:]))
else:
    print('Opção inválida! Tente novamente.')
    
    
#Desafio 38-comparara 2 números e dizer maior, menor ou =

n1 = int (input ('Digite o primeiro número: '))
n2 = int (input ('Digite o segundo número:  '))
if n1 > n2:
    print ('O número {} é MAIOR que {}.'.format (n1, n2))
elif n1 < n2: 
    print ('O número {} é MENOR que {}.'.format (n1, n2))
else:
    print ('Os números são IGUAIS.')
    
#Desafio 39-alistamento militar
    
ano_atual = int(input('Digite o ano atual: '))
ano_nascimento = int(input("Digite seu ano de nascimento: "))
idade = ano_atual - ano_nascimento
ano_para_se_alistar = ano_atual + (18 - idade)
if idade == 18:
    print('Você deve se alistar esse ano. Procure a Junta Militar mais próxima de sua residência.'.upper())
elif idade < 18:
    print('Você deve se alistar em {}.'.format(ano_para_se_alistar).upper())
else:
    print('Você precisa se alistar IMEDIATAMENTE. Procure a Junta Militar mais próxima de sua residência.'
          
  #outra forma de fazer      
from datetime import date #não precisa digitar o ano atual
atual = date.today().year
nasc = int (input ('Ano de nascimento: '))
idade = atual - nasc
print ('Quem nasceu em {} tem {} anos em {}.'.format (nasc,idade,atual))
if idade == 18:
    print ('Você tem de se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade 
    print ('Ainda faltam {} anos para o alistamento.'.format (saldo))
    ano = saldo + atual
    print ('Seu alistamento será em {}.'.format (ano))
else:
    saldo = idade - 18 # posso chamar de saldo porque está dentro da identação
    print ('Você já deveria ter se alistado há {} anos.'.format (saldo))
    ano = atual - saldo# posso dar o memso nome devido a identação
    print ('Você deveria ter se alistado em {}.'.format (ano))
