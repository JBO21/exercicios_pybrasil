def calc_multa():

    print("#-"*5, "Calculo para multa de Pesca", "#-"*5)
    print()
    quilos = float(input("Quantos kilos foram pescados? "))
    exced = quilos - 50
    print("=-"*20)
    if exced > 0:
        multa = exced * 4
        print(f"\033[0:31mPesca excedeu {exced}kg."
              f"\nDeve ser pago o valor de R$ 4,00 por kg excedido "
              f"\nPescador precisa pagar multa no valor de R$ {multa:.2f}!")
    else:
        print(f"\033[0:32mComo sua pesca apresentou o peso de {quilos} kg "
              f"não excedeu o limite de 50 kg. Não incidindo multa!")


calc_multa()
