maior = 0
menor = 0
aux = 0
for c in range(1,6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(c)))
    if peso > maior:
        maior = peso
        menor = maior
    elif peso <= menor:
        menor = peso

print('O maior peso foi {:.2f} Kg e o menor {:.2f} kg.'.format(maior, menor))