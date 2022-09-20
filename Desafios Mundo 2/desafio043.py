p = float(input('Digite o peso: '))
a = float(input('Digite a altura: '))
imc = p/(a**2)
if imc < 18.5:
    print('\033[1;34mABAIXO DO PESO')
elif imc >= 18.5 and imc < 25:
    print('\033[1;34mPESO IDEAL')
elif imc >=25 and imc < 30:
    print('\033[1;34mSOBREPESO')
elif imc >= 30 and imc < 40:
    print('\033[1;34mOBESIDADE')
else:
    print('\033[1;34mOBESIDADE MÓRBIDA')