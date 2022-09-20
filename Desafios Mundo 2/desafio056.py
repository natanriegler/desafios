si = 0
idademv = 0
maisde20 = 0
for c in range(1,5):
    nome = input('Insira o nome da {}ª pessoa: '.format(c))
    idade = int(input('Insira a idade da {}ª pessoa: '.format(c)))
    sexo = input('Insirao sexo da {}ª pessoa: '.format(c))
    print('='*45)
    si = si + idade
    if sexo == 'masculino':
        if idade >= idademv:
            maisvelho = nome
            idademv = idade
    else:
        if idade < 20:
            maisde20 += 1


print('A média de idade do grupo é {:.0f}.'.format(si/4))
print('O nome do homem mais velho é {}'.format(maisvelho))
print('{} mulheres tem menos de 20 anos'.format(maisde20))
print('=' * 45)
