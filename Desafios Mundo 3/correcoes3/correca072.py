cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'trese', 'quatorze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')

while True:
    núm = int(input('Digite um número entre 0 e 20: '))
    if 20 >= núm >= 0:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {cont[núm]}')