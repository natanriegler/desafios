contagem  = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
             'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um número (entre 0 e 20): '))
    if 20 >= n >= 0:
        print(f'Você digitou o número {contagem[n]}')
        break
    else:
        print('Número não está entre 0 e 20 TENTE NOVAMENTE')