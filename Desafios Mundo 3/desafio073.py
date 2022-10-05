tabela = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians',
          'Flamengo', 'Atlético Paranaense', 'Atlético Mineiro', 'América',
          'Fortaleza', 'Bota-Fogo', 'Santos', 'Goiás',
          'São Paulo', 'Bragantino', 'Coritiba', 'Ceará',
          'Cuiaba', 'Avaí', 'Atlético Goianiense', 'Juventude')

print('=-'*30)
print('Lista de times do Brasileirão: ', tabela)
print('=-'*30)
print('Os 5 primeiros são: ', tabela[0:5])
print('=-'*30)
print('Os 4 últimos são: ', tabela[16:20])
print('=-'*30)
print('Times em ordem alfabética: ', sorted(tabela))
print('=-'*30)
for i in range(0, len(tabela)):
    if tabela[i] == 'Chapecoense':
        p = i
        print(f'O Chapecoense está na {p}ª posição')
    else:
        print('A Chapecoense não está entre os 20 primeiros')
        break

