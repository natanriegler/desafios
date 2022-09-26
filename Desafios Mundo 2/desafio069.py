mais18 = 0
masc = 0
femmen20 = 0
while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo (M/F): ')).upper().strip()[0]
    print('-' * 30)
    r = str(input('Quer continuar ou não? (S/N): ')).upper().strip()
    if idade > 18:
        mais18 += 1
    if sexo == 'M':
        masc += 1
    elif sexo == 'F':
        if idade < 20:
            femmen20 += 1
    if r == 'N':
        print(f'''Foram cadastradas {mais18} pessoas com mais de 18 anos
        Foram cadasttrados {masc} homens
        Foram cadastradas {femmen20} mulheres com menos de 20 anos''')
        break
