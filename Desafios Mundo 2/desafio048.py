s = 0
vs = 0
for n in range(1,501, 2):
    #NÃO HAVIA COLOCOCADO O 3° CRITERIO NO RANGE PARA PEGAR APENAS NÚMEROS IMPARES range(1, 501, -)
    if n % 3 == 0:
        vs = vs + 1
        s = s + n
print('A soma dos {} valores solicitados é {}'.format(vs, s))
