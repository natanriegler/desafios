nome = str(input('Digite seu nome completo: '))
print('- Seu nome com todas as letras maiúsculas: {}'.format(nome.upper()))
print('- Seu nome com todas as letras minúsculas: {}'.format(nome.lower()))
list = nome.split()
nome = ''.join(list)
print('- Qtd. de letras no nome: {}'.format(len(nome)))
print('- Qtd. letras primeiro nome: {}'.format(len(list[0])))