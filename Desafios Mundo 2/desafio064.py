tot = 0
soma = 0
v = 0
while not v == 999:
    v = int(input('Digite um número: '))
    if v != 999:
        soma = soma + v
        tot = tot + 1
print('A o total foram digitatos {} número e a some entre eles é {}'.format(tot, soma))