n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
if m < 5:
    print('\033[1;31mREPROVADO')
elif m <= 6.9:
    print('\033[1;33mRECUPERAÇÃO')
else:
    print('\033[1;32mAPROVADO')