from random import randint
from time import sleep
n1 = randint(0,5)
print('Pensando um número...')
sleep(3)
n2 = int(input('Em qual número pensei?: '))
if n1 == n2:
    print('Parabéns o número que pensei era realmente {}'.format(n1))
else:
    print('Que pena, na verdade eu pensei no número {}'.format(n1))
