from random import randint
while True:
    computador = randint(1, 10)
    jogador = int(input('Digite um número: '))
    op = str(input('Par ou Ímpar (P/I): ')).upper().strip()
    soma = computador + jogador
    print(f'Jogador digitou {jogador} computador escolheu {computador}')
    if soma%2 == 0:
        r = 'PAR'
    else:
        r = 'ÍMPAR'
    print(f'Deu {r}')

    if op == 'I' and r == 'PAR':
        print('Você perdeu!')
        break
    elif op == 'P' and r == 'ÍMPAR':
        print('Você perdeu!')
        break
    else:
        print('Você venceu!')
    '''if op != r:
        print('Você perdeu!')
        break
    else:
        print('Você venceu!')'''

