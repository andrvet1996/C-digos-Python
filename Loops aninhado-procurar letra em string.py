str_list=['João','Roberto', 'Rafael']# encontra as letras em uma string
for nome in str_list:
    for c in nome:
        if c in 'r':#aqui vc coloca a letra que está pesquisando
            print (c)
