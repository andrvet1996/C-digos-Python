def maior_num(l, n):#maior número
  maior = l[0]

  if n > 1:
    maior = maior_num(l[1:], n - 1)

  if l[0] > maior:
    return l[0]

  return maior

def soma_num(l, n):#soma
  soma = l[0]

  if n > 1:
    soma += soma_num(l[1:], n - 1)

  return soma

print(soma_num([10, 20, 50, 10, 10], 5))
print(maior_num([5, 3, 10, 9], 4))
