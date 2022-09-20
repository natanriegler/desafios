from math import factorial
n = int(input('Digite um número: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))
while not n == 0:
    if n == 1:
        print(n, '= ', f)
    else:
        print(n, ' X  ', end='')
    n = n-1
