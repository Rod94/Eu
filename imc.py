#saber o imc da pessoa e indicar o nivel em que ela está.
nome = input("Informe o seu nome: ")
alt = float(input("Informe sua altura: "))
peso = float(input("Informe seu peso: "))

imc = peso / (alt*alt)
print("{} seu imc é {:.2f}!".format(nome,imc))
if imc < 17:
    print("Você esta muito abaixo do peso")
elif imc >= 17 and imc <= 18.49:
    print("Você está abaixo do peso")
elif imc >= 18.5 and imc <= 24.99:
    print("Você esta no seu peso normal")
elif imc >= 25 and imc <= 29.99:
    print("Você esta acima do peso")
elif imc >= 30 and imc <= 34.99:
    print("Você esta em Obesidade I")
elif imc >= 35 and imc <= 39.99:
    print("Voce está em Obesidade II(severa)")
else:
    print("Voce esta em Obesidade III(mórbida)")

