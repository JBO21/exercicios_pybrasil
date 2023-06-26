# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

def genero():
    sexo = str(input('Qual o seu gênero (M/F)? ')).upper().strip()
    if sexo == 'F':
        print('Você é do sexo Feminino')

    elif sexo == 'M':
        print('Você é do sexo Masculino')
    else:
        print('Sexo inválido')

genero()