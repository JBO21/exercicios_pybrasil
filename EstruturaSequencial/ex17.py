def venda_tinta():

    print("#-"*5, "Calculo de tinta", "#-"*5)
    print()

    parede = float(input("Tamanho da área a ser pintada(em m2)? "))
    litro = parede // 6
    latar = litro % 18
    latar2 = litro % 3.6
    lata18 = litro // 18
    latade18 = lata18
    lata3 = litro // 3.6
    dlata = (latar*1.1) // 3.6
    dlata = int(dlata)

    if latar > 0:
        lata18 += 1
        latar = 1
    elif latar2 > 0:
        lata3 += 1

    custo1 = lata18 * 80
    custo2 = lata3 * 25
    custo3 = (latade18 * 80) + (dlata * 25)
    print()
    print("-=" * 20)
    print("Cliente, tem as seguintes opções:")
    print()
    print(f" - {lata18:.0f} lata(s) de 18 litros, por R$ {custo1:.2f}, ou")
    print(f" - {lata3:.0f} lata(s) de 3.6 litros, por R$ {custo2:.2f}, ou")
    print(f" - {latade18:.0f} lata(s) de 18 litros e {dlata:.0f} lata(s) de 3.6 litros, por R$ {custo3:.2f}")


venda_tinta()