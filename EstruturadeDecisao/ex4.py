# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

def consoante():
    letra = input('Digite um letra: ').upper().strip()
    vogais = ['A', 'E', 'I', 'O', 'U']
    if letra in vogais:
        print(f'{letra} é uma vogal!')
    else:
        print(f'{letra} é uma consoante!')

consoante()