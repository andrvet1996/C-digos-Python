a=eval(input('digite lado 1:'))
b=eval(input('digite lado 2:'))
c=eval(input('digite lado 3:'))

maior_lado=0
if a>maior_lado:
    maior_lado=a
if b>maior_lado:
    maior_lado=b
if c>maior_lado:
    maior_lado=c

if maior_lado<(a+b+c)-maior_lado:
    print('os lados formam um triângulo')
    if a==b and b==c and a==c:
        print('triângulo equilátero')
    elif a!=b and b!=c and a!=c:
        print('triângulo escaleno')
    else:
        print('triângulo isosceles')

else:
    print ('os lados não formam um triângulo')
