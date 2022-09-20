s = cont = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'Foram digitados {cont} e a soma entre eles foi {s}')