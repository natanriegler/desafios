s = float(input('Qual o salário?: '))
if s > 1250.00:
    print('O seu salário passará a ser R$ {}'.format(s+(s/100)*10))
else:
    print('O seu salário passará a ser R$ {}'.format(s+(s/100)*15))