def numeros():
    n1 = int(input("Digite o primeiro número inteiro: "))
    n2 = int(input("Digite o segundo número inteiro: "))
    n3 = float(input("Digite um número real(com casa decimal): "))
    op1 = (n1*2) * (n2/2)
    op2 = (n1*3) + n3
    op3 = n3**3
    print(f"""O produto do dobro do primeiro número com a metade do segundo é: {op1}
A soma do triplo do primeiro número com o terceiro é: {op2}
O terceiro número elevado ao cubo é: {op3:.2f}""")


numeros()
