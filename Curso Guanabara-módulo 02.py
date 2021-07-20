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
