nam = 0
am = 0
for c in range(1, 8):
    i = int(input('Digite o {}° idade: '.format(c)))
    if i < 21:
        nam = nam + 1
    else:
        am = am + 1
print('Das 7 pessoas {} não atingiram a maioridade e {} atingiram.'.format(nam, am))