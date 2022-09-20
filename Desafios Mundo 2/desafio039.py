idade = int(input('Digite quantos anos você tem: '))
if idade < 18:
    print('\033[1;32mVocê ainda vai se alistar no serviço militar... Ainda faltam {} ano(s)...'.format(18-idade))
elif idade == 18:
    print('\033[1;33mAgora é a hora de se alistar no serviço militar!')
else:
    print('\033[1;31mJá passou do tempo de você se alistar no serviço militar! Você está {} ano(s) atrasado!'.format(idade-18))