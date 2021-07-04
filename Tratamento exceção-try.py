#tratamento de exceção

a=2
b=0

try:
    #print (a/b)
    print (a/a)

except: 
    print ("Não é permitida divisão por zero.")#ocorrerá se a condição for 
    #absurda como em a/b
