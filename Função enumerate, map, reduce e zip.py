#função enumerate: lista e índice

lista = ["abacate", "bola", "cachorro"]

for i, nome in enumerate (lista):
    print (i,nome)
    
    
    
#função map: aplicada a função a todos os elementos da lista

def dobro(x):
    return x*2
    
valor = [1, 10, 20, 30, 40]

valor_dobrado = map (dobro, valor)

valor_dobrado = list (valor_dobrado)
print (valor_dobrado)



#função reduce: reduz uma lista a um único valor

from functools import reduce

def soma (x,y):
    return x+y
    
lista = [100, 200, 300, 400]

soma = reduce (soma, lista)
print (soma)


#função zip: concatena listas

lista1 = ["USP","UNICAMP", "UNESP", "UFV", "UNIVESP"]
lista2 = ["Quimica", "Veterinaria", "Odontologia", "Direito", "Biomedicina"]
lista3 = [1,2,3,4,5]

for universidade, curso, valor in zip (lista1, lista2, lista3):
    print (universidade, curso, valor)
