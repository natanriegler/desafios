valores = list()
posmai = list()
posmen = list()
menor = maior = 0
for c in range(0,5):
    valores.append(int(input('Digite um valor: ')))
    if c == 0:
        menor = valores[c]
        maior = valores[c]
    if valores[c] > maior:
        maior = valores[c]
        posmai.pop()
        posmai.append(c)
    elif valores[c] == maior:
        maior = valores[c]
        posmai.append(c)
    if valores[c] < menor:
        menor = valores[c]
        posmen.pop()
        posmen.append(c)
    elif valores[c] == menor:
        menor = valores[c]
        posmen.append(c)
print('O maior valor digitado foi {} nas posições {}'.format(maior, posmai))
print('O menor valor digitado foi {} nas posições {}'.format(menor, posmen))