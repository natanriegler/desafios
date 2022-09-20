from datetime import date
an = int(input('Digite o ano de nascimento: '))
aa = int(date.today().year)
i = aa - an
if i <= 9:
    print('\033[1;34mMIRIM')
elif i <= 14:
    print('\033[1;34mINFANTIL')
elif i <= 19:
    print('\033[1;34mJUNIOR')
elif i <= 20:
    print('\033[1;34mSÊNIOR')
else:
    print('\033[1;34mMASTER')