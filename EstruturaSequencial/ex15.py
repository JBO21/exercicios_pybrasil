def calc_sal():
    print("#-"*5, "Calculo de salário mensal", "#-"*5)
    print()

    valorh = float(input("Qual valor recebido por hora? "))
    horas = float(input("Quantas horas trabalhadas no mês? "))
    salb = valorh * horas
    ir = salb * 0.11
    inss = salb * 0.08
    sind = salb * 0.05
    sal = salb - ir - inss - sind
    print(f"""\033[0:32m+ Salário Bruno: R$ {salb:.2f}\033[m
    \033[0:31m- IR (11%): R$ {ir:.2f}
    - INSS (8%): R$ {inss:.2f}
    - Sindicato (5%): R$ {sind:.2f}\033[m
    = Salário Líquido: R$ {sal:.2f}""")

calc_sal()