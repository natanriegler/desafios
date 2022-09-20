n = str(input('Digite um número: '))
cont = len(n)
if cont == 1:
    print(' unidade: {}'.format(n))
elif cont == 2:
    print(' unidade: {} \n dezena: {}'.format(n[1], n[0]))
elif cont == 3:
    print(' unidade: {} \n dezena: {} \n centena: {}'.format(n[2], n[1], n[0]))
elif cont == 4:
    print(' unidade: {} \n dezena: {} \n centena: {} \n milhar: {}'.format(n[3], n[2], n[1], n[0]))