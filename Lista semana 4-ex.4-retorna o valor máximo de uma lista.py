def f(v, i):
    if i == 0:
        return v[i]
    else:
        return max(v[i], f(v, i - 1)) #retorna valor máximo


l = [5, 45, 6, 8, 1, 2] #lista
print(f(l, len(l) - 1))