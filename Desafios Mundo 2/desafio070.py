totcomp = prod1000= men = cont = 0
while True:
    cont += 1
    nome_prod = str(input('Nome do produto: '))
    preco_prod = float(input('Preço do produto: R$ '))
    if cont == 1:
        men = preco_prod
        prodbarato = nome_prod
    elif preco_prod <= men:
        men = preco_prod
        prodbarato = nome_prod
    resp = ' '
    totcomp += preco_prod
    if preco_prod > 1000.00:
        prod1000 += 1
    while resp not in 'SN':
        resp = str(input('Quer continuar?: [S/N] ')).upper().strip()[0]
    if resp == 'N':
        print(f'O total da compra foi {totcomp}')
        print(f'Temos {prod1000} produtos cusrtando mais de R$1000.00')
        print(f'O produto mais barato foi {prodbarato} que custou {men}')
        break