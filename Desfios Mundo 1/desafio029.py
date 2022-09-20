v = int(input('Digite a velocidade em Km/h: '))

e = v - 80
if e > 0:

    print('Sua velocidade foi de {} Km/h. Você foi multado! \nO valor da sua multa será de R${}'.format(v, e*7))
else:
    print('Sua velocidade foi de {} Km/h você não foi multado.'.format(v))


