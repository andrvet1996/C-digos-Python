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
          
          
   #Desafio 30-cálculo média
#n1 = float (input ('Digite a primeira nota: '))
#n2 = float (input ('Digite a segunda nota:  ')) 
#média =  (n1 + n2) / 2
#if média < 5.0:
    #print ('Você foi REPROVADO, pois a média {:.1f} é menor que 5.0.'.format (média))
#elif média > 7.0:
    #print ('Você foi APROVADO, pois a média {:.1f} é maior que 7.0. Parabéns!'.format (média))
#else:
    #print ('Você está em RECUPERAÇÃO, pois a média {:.1f} está entre 5.0 e 6.9.'.format (média))
    
#outra forma
n1 = float (input ('Digite a primeira nota: '))
n2 = float (input ('Digite a segunda nota:  ')) 
média =  (n1 + n2) / 2
if média < 5.0:
    print ('Você foi REPROVADO, pois a média {:.1f} é menor que 5.0.'.format (média))
elif média >=5.0 and média <7.0:
    print ('Você está em RECUPERAÇÃO, pois a média {:.1f} está entre 5.0 e 6.9.'.format (média))
else:
    print ('Você está APROVADO, pois a média {:.1f} é maior que 7.0. Parabéns!!!'.format (média))
          
          
 #Desafio 41-categoria de atletas
from datetime import date
data_atual = date.today().year
nome = str (input ('Nome completo do atleta: '))
dn = int (input ('Ano de nascimento: '))
idade = data_atual - dn
if idade <= 9:
    print ('O atleta {} tem {} anos e pertence a categoria MIRIM.'.format (nome,idade))
elif 9< idade <=14:
    print ('O atleta {} tem {} anos e pertence a categoria INFANTIL.'.format (nome,idade))
elif 15< idade <=19:
    print ('O atleta {} tem {} anos e pertence a categoria JUNIOR.'.format (nome,idade))
elif 20< idade <=25:
    print ('O atleta {} tem {} anos e pertence a categoria SÊNIOR.'.format (nome,idade))
else:
    print ('O atleta {} tem {} anos e pertence a categoria MASTER.'.format (nome,idade))
          
          
#Desafio 42-analisador de triângulo
print('#' * 24)
print('Analisador de triângulos')
print('#' * 24)
a: float = float(input('Valor do primeiro segmento: '))
b = float(input('Valor do segundo segmento:  '))
c = float(input('Valor do terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos {}, {} e {} FORMAM UM TRIÂNGULO.'.format(a, b, c))
    if a == b == c:#não coloque elif,pois há duas possibilidades é ou não é triângulo
        #esse if está identado desse jeito porque está ligado ao tipo de triângulo
        print('O triângulo é EQUILÁTERO.')
    elif a != b and b != c and c != a:
        print('O triângulo é ESCALENO.')
    else:
        print('O triângulo é ISÓSCELES.')
else:
    print('Os segmentos {}, {} e {} NÃO FORMAM UM TRIÂNGULO')
          
#Desafio 43-IMC
peso = float (input ('Digite o seu peso (Kg): '))
alt = float (input ('Digite sua altura (m): '))
imc = peso / (alt**2)
if imc < 18.5:
    print ('Seu IMC é {:.1f}. Você está ABAIXO DO PESO IDEAL.'.format (imc))
elif 18.5 <= imc < 25.0:
    print ('Seu IMC é {:.1f}. O seu peso está NORMAL.'.format (imc))
elif 25.0 <= imc <  30.0:
    print ('Seu IMC é {:.1f}. Você está com SOBREPESO.'.format (imc))
elif 30.0 <= imc < 40.0:
    print ('Seu IMC é {:.1f}. Você está OBESO.'.format (imc))
else:
    print ('Seu IMC é {:.1f}. Você está com OBESIDADE MÓRBIDA.'.format (imc))
          
#Desafio 43-Descontos na loja
print('=' * 13)
print('LOJA DO ANDRÉ')
print('=' * 13)
preço = float(input('Preço das compras: R$ '))
print('''Condições de pagamento:
[1] à vista dinheiro/cheque 
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
condição = int(input('Escolha a forma de pagamento: '))
if condição == 1:
    desc = preço - (0.1 * preço)
    print('O valor a pagar, com o desconto de 10%, é de R${:.2f}.'.format(desc))
elif condição == 2:
    desc = preço - (0.05 * preço)
    print('O valor a pagar, com o desconto de 5%, é de R${:.2f}.'.format(desc))
elif condição == 3:
    parcela = preço / 2
    print('O valor a pagar, sem desconto, é de R${:.2f}, dividido em duas parcelas de R${:.2f}.'.format(preço, parcela))
elif condição == 4:
    acresc = preço + (0.20 * preço)
    parcelas = int(input('Número de parcelas: '))
    cada_parcela = acresc / parcelas
    print('O valor a pagar, com acréscimo de 20%, é de R${:.2f}, dividido em {} de R${:.2f}.'.format(acresc, parcelas, cada_parcela))
else:
    print('Opção \033[1;31mINVÁLIDA!\033[m Tente novamente.')#letra vermelha
    
          
  #Aula 13-LAÇOS DE REPETIÇÃO
#for c in  range (0, 6):#repete oi 6x
    #print ('Oi!')
#print ('FIM!')

#contagem
#for c in range (1, 6):#conta mas não imprimi o último número
    #print (c)
#print ('FIM!')

'''#contagem para trás
for c in range (0, 6, -1): 
    print (c)#acrescenta -1 para contar para trás
print ('FIM!')

#contagem pulando
for c in range (0, 6, 2): 
    print (c)#conta e pula de 2 em 2
print ('FIM!')'''

#n = int (input ('Digite um número: '))
#for c in range (0, n):#usuário define a contagem, mas não conta o último
    #print (c)
#print ('FIM!')

#n = int (input ('Digite um número: '))
#for c in range (0, n+1):#usuário define a contagem, conta o último n+1
    #print (c)
#print ('FIM!')

#i = int (input ('Início: '))#define início (i), contagem total (f+1) e pulos (p)
#f = int (input ('Fim:    '))
#p = int (input ('Passo:  '))
#for c in range (i, f+1, p):
    #print (c)
#print ('FIM!')

#for c in range (0, 4):
    #n = int (input ('Digite um número: '))# repetir o input n vezes
#print ('FIM')

soma = 0
for c in range (0, 4):
    n = int (input ('Digite um valor: '))
    soma += n # soma += n é o mesmo que soma = soma + n
print ('O somatório de todos os números digitados é {}.'.format (soma))
          
          
#Desafio 46-contagem regressiva
from time import sleep
for c in range (10, -1, -1):# o primeiro -1 faz a contagem chegar a zer
    print (c)
    sleep (0.5)#espera 1s entre os números
sleep (1)#espera 1s até o BUM
print ('BUM! BUM! BUM!')
