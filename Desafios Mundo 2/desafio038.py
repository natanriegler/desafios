n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 < n2:
    print('\033[1;32mO segundo valor é  maior')
elif n1 == n2:
    print('\033[1;32mNão existe valor maior, os dois são iguais')
else:
    print('\033[1;32mO primeiro valor é maior')