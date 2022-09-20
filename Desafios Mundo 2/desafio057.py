sexo = ''
while not sexo == 'M' or sexo == 'F':
    sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()
print('O sexo digitado foi {}'.format(sexo))
