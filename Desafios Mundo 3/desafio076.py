print('-'*45)
print('{:^45}'.format('LISTA DE PREÇOS'))
print('-'*45)
produto = ('Lápis', 'Borracha', 'Caderno', 'Estojo',
           'Transferidor', 'Compasso', 'Mochila', 'Canetas',
           'Livro')
valor = (1.75, 2.00, 15.90, 25.00,
           4.20, 9.99, 120.32, 22.30,
           34.90)
for c in range(1,9):
    print('{:.<30}{:.>15}'.format(produto[c],f'R$ {valor[c]}'))
print('-' * 45)