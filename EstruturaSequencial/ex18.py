def calc_down():
    arquivo = float(input("Qual o tamanho do arquivo para download?(em MB) "))
    veloc = float(input("Qual a velocidade da internet para download?(em MB/s) "))
    segundos = arquivo / veloc
    minutos = segundos // 60
    seg = segundos % 60
    print()
    print("=-" * 20)
    print(f"\033[0;33mO arquivo de {arquivo}MB que esta querendo baixar a uma velocidade de {veloc}MB/s,"
          f" vai ser finalizado em {minutos} minutos e {seg} segundos\033[m")


calc_down()
