from random import randint
maior = menor = 0
lista = (randint(1, 10),randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print('Os valores sorteados foram: ', end=' ')
for c in range(0, 5):
    print(lista[c], end=' ')
    if c == 1:
        maior = lista[c]
        menor = maior
    else:
        if lista[c] >= maior:
            maior = lista[c]
        if lista[c] <= menor:
            menor = lista[c]
print(f'\nO maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')

