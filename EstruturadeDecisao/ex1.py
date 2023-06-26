# Faça um Programa que peça dois números e imprima o maior deles.

def qual_maior():
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    if n1 > n2:
        print(f' O maior número digitado é: ', (n1))
    else:
        print(f' O maior número digitado é: ', (n2))

qual_maior()
