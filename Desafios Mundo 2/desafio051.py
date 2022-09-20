print('='*40)
print('10 PRIMEIROS TERMOS DE UMA PA'.format('{:=^40}'))
print('='*40)
pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
for c in range(1, 11):
    pt = pt + r
    print(pt, end=' => ')
print('ACABOU!')
