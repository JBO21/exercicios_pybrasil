#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.


def sinal():
    num = float(input('Digite um número: '))
    if num > 0:
        print(f'O número {num} é positivo!')
    else:
        print(f'O número digitado, {num}, é negativo! ')


sinal()