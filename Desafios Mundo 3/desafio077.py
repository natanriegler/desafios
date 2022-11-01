palavra = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON',
            'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR',
            'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
vogal = ('A', 'E', 'I', 'O', 'U')

for pos in range(0, len(palavra)):
    print(f'\nNa palavra {palavra[pos]} temos ', end='')
    for c in range(0,len(vogal)):
        if vogal[c] in palavra[pos]:
            print(f'{vogal[c]} ', end='')