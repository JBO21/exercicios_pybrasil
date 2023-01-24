def salario():
    valor_hora = float(input("Qual o valor você recebe por hora? "))
    numh = float(input("Quantas horas trabalhou este mês? "))
    print(f"Seu salário para este mês será de R$ {valor_hora * numh:.2f}")

salario()