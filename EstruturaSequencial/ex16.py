def compra_tinta():
    print("#-"*5, "Calculo de tinta", "#-"*5)
    print()

    parede = float(input("Tamanho da área a ser pintada(em m2)? "))
    cobertura = parede // 3
    tinta = 0
    if cobertura == 18:
        tinta = 1
    if cobertura > 18:
        tinta = cobertura / 18
        if tinta % 18 > 0:
            tinta += 1
            tinta = int(tinta)
    else:
        tinta = 1
    custo = tinta * 80

    print(f" Para uma área de {parede:.0f}m2, será necessario {cobertura} litros de tinta "
          f"o que corresponde a {tinta:.0f} lata(s) de tinta. \n Com isso o custo total é R${custo:.2f}")

compra_tinta()