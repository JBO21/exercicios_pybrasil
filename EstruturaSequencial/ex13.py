def peso():
    h = float(input("Qual a sua altura? "))
    conta_h = (72.7*h) - 58
    conta_m = (62.1*h) - 44.7
    print(f" O peso ideal para uma mulher desta altura é {conta_m:.3f} kg e para um homem é {conta_h:.3f} kg.")


peso()
