#x = [1,2,3,4,5]
#y = []

#for i in x:
    #y.append(i**2)
    
    #print(x)
    #print(y)
    
# list comprehension é uma alternativa ao comando acima
#x = [1,2,3,4,5]
#y = [for i**2 for i in x]

#print(x)
#print(y)

w = [1,2,3,4,5]
z = [i for i in w if i%2==1]

print (w)
print (z)
