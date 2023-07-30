def menor_valor():

    n1 = float(input('Preço do primeiro produto: R$ '))
    n2 = float(input('Preço do segundo produto: R$ '))
    n3 = float(input('Preço do terceiro produto: R$ '))

    if n1 < n2 and n1 < n3:
        print(f"O produto de menor valor é o primeiro produto, no valor R$ {n1}")
    elif n2 < n3 and n2 < n1:
        print(f"O produto de menor valor é o segundo produto, no valor R$ {n2}")
    else:
        print(f"O produto de menor valor é o terceiro produto, no valor R$ {n3}")


menor_valor()
