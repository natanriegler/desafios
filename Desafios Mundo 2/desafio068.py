from random import randint
while True:
    computador = randint(1, 10)
    jogador = int(input('Digite um número: '))
    op = str('Par ou Ímpar [P/I]: ')
    if op == 'Ii' and jogador % 2 == 0:
        print('')