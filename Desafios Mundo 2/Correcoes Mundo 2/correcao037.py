num  = int(input('Digite um número inteiro: '))
print('''ESCOLHA UMA DAS BASES PARA COVERSÃO
[1]CONVERTER PARA BINÁRIO
[2]CONVERTER PARA OCTAL
[3]CONVERTER PARA HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} covertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção Inválida. Tente novamente')