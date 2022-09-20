d = float(input('Qual a distância de sua viagem em Km: '))
if d <= 200:
    print('O preço da passagem é R${}'.format(0.5*d))
else:
    print('O preço da passagem é R${}'.format(0.45*d))
    