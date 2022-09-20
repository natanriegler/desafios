cidade = str(input('Digite o nome da cidade: '))
r = cidade.find('Santo')
if r >= 0:
    print('Começa com Santo?: Sim')
else:
    print('Começa com Santo?: Não')