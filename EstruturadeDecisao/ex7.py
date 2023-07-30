def qual_maior():

    n1 = float(input('Primeiro número: '))
    n2 = float(input('Segundo número: '))
    n3 = float(input('Terceiro número: '))

    if n1 > n2 and n1 > n3:
        print (f"O maior número é {n1}")
    elif n2 > n3 and n2 > n1:
        print (f"O maior número é {n2}")
    else:
        print (f" o maior número é {n3}")


qual_maior()