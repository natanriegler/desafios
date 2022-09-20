casa = float(input('Valor da Casa: R$'))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento?: '))
prestação = casa / (anos*12)
mínimo = salário * 30/100
print('Para pagar a casa de {:.2f} em {} anos '.format(casa, anos), end='')
print('A prestação será de {:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')