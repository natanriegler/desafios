vc = float(input('Digite o valor da casa: '))
sc = float(input('Digite o seu salário: '))
p = int(input('Digite em quantos anos vai pagar: '))

vp = vc/(p*12)

if vp > (sc/100*30):
    print('\033[1;31mSeu  empréstimo foi negado!')
else:
    print('\033[1;32mSeu empréstimo foi aprovado!')