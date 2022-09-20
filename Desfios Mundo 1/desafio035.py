r1 = int(input('Digite o primeiro lado: '))
r2 = int(input('Digite o segundo lado: '))
r3 = int(input('Digite o terceiro lado: '))
if r1 > r2 and r3:
    mai = r1
    if r2 + r3 >= r1:
        print('É possível formar um triângulo!')
    else:
        print('Não é possível formar um triângulo!')
elif r2 > r1 and r3:
    mai = r2
    if r1 + r3 >= r2:
        print('É possível formar um triângulo!')
    else:
        print('Não é possível formar um triângulo!')
elif r3 > r2 and r1:
    mai = r3
    if r2 + r1 >= r3:
        print('É possível formar um triângulo!')
    else:
        print('Não é possível formar um triângulo!')
else:
    print('É possível formar um triângulo!')