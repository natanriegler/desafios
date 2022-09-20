
while True:
    n = int(input('Diite o número para a tabuada: '))
    if n < 0:
        break
    for c in range(1, 11):
        p = n*c
        print(f'{n} X {c} = {p}')
print('Foi digitado um número NEGATIVO. O programa foi finalizado.')