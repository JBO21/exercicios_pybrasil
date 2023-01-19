def nota_media():
    n1 = int(input(" Primeira Nota: "))
    n2 = int(input(" Segunda Nota: "))
    n3 = int(input(" Terceira Nota: "))
    n4 = int(input(" Quarta Nota: "))
    media = (n1+n2+n3+n4)/4
    print(f'A media foi: {media:.1f}')

nota_media()
