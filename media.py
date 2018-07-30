#Media de uma faculdade com a oportunidade de fazer a terceira prova caso nao atinja a >=6
n1 = float(input("Informe a primeira nota do semestre: "))
n2 = float(input("Informe a segunda nota do semestre: "))
media = (n1 + n2)/2

if media >= 6:
    print("Parabens, sua nota foi {} e voce passou de semestre!!".format(media))
else:
    print("A sua nota foi {} e voce ficou de recuperação e voce tem a oportunidade de fazer a terceira prova!".format(media))
    n3 = float(input("Informe sua terceira nota: "))
    if n1 > n2 and n3 > n2:
        media2 = (n1 + n3)/2
        print("Parabéns, sua media do semestre foi {} e voce conseguiu passar.".format(media2))
    else:
        media3 = (n2 + n3)/2
        print("Sua media do semestre foi {} e voce nao conseguiu passar.".format(media3))
