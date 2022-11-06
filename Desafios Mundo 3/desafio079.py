valores = list()
r=''
c=0
while not r == 'N':
    valores.append(int(input('Digite um valor: ')))
    if valores[len(valores)-1] in valores[0:c]:
        print('Valor duplicado! Não vou adicionar...')
        valores.pop()
    else:
        print('Valor adicionado com sucesso...')
    c += 1
    r = str(input('Quer continuar [S/N]: ')).strip().upper()
print('-='*35)
print(f'Você digitou os valores {valores}')