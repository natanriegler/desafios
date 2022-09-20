from random import randint
from time import sleep
comp = randint(1, 10)
totp = 0
print('Estou pensando em um número...')
sleep(1)
print('Pronto!')
sleep(1)
palpite = 0
while not palpite == comp:
    palpite = int(input('Digite um palpite: '))
    totp = totp + 1
print('O computador pensou o número {}'.format(comp))
print('Foram necesários {} palpites para você acertar.'.format(totp))