a=eval(input('Digite sua altura em metros:'))
b=eval(input('Digite seu peso em Kg :'))

imc=b/a**2

print('Seu imc é:')

if imc<18.5:
    print('Abaixo do peso imc<18.5')

elif imc>25.0:
    print('Sobrepeso imc>25.0')

else:
    print('Peso normal 18.5<imc<25.0')

print('Se vc estiver com sobrepeso ou abaixo do peso procure orientação médica')





