op = 4
while not op != 4:
      n1 = int(input('Digite o 1º valor: '))
      n2 = int(input('Digite o 2º valor: '))

      print('='*30,'\nDgite uma das opções:\n'
            '[1] SOMAR\n'
            '[2] MULTIPLICAR\n'
            '[3] MAIOR\n'
            '[4] NOVOS NÚMEROS\n'
            '[5] SAIR DO PROGRAMA')
      op = int(input('Opção: '))
      if op == 1:
            print('{} + {} = {}'.format(n1, n2, (n1+n2)))
      elif op == 2:
            print('{} X {} = {}'.format(n1, n2, (n1*n2)))
      elif op == 3:
            if n1 > n2:
                        print('O maior é o número'.format(n1))
            elif n1 == n2:
                  print('Os dois são iguais!')
            else:
                  print('O maior é o número {}'.format(n2))
      elif op == 5:
            print('Programa encerrado.')
