# Faça um Programa que leia três números e mostre o maior deles

def num_maior():
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    num3 = float(input('Digite o terceiro número: '))
    #maior = max(num1, num2, num3)
    if num1 > num2 and num1 > num3:
        print(num1)
    elif num2 > num1 and num2 > num3:
        print(num2)
    elif num3 > num2 and num3 > num1:
        print(num3)
    #print(maior)


num_maior()
