N1=input('Digite a sua nota 1:')
N2=input('Digite sua nota 2:')
nt1=eval(N1)
nt2=eval(N2)

print (f'A média é: {media}')media=(0.4*nt1)+(0.6*nt2)

if media>=5.0:
    print('Você foi aprovado.Parabéns!!!')
    
else:
    print('Você foi reprovado. É preciso estudar mais')
