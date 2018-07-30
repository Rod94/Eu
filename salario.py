sh = int(input("Informe quanto voce ganha por hora:"))
th = int(input("Informe quantas horas foram trabalhadas no mês:"))
salario_bruto = sh * th
print(f"Salario bruto foi de R${salario_bruto:.2f}")
inss = salario_bruto * 8/100
print(f"Valor INSS foi de R${inss:.2f}")
ir = salario_bruto * 11/100
print(f"Valor do imposto de renda foi de R${ir:.2f}")
sindicato = salario_bruto * 5/100
print(f"Valor cobrado pelo sindicato foi de R${sindicato:.2f}")
descontos = inss + ir + sindicato
salario_liquido = salario_bruto - descontos
print(f"O salario liquido do mês foi de R${salario_liquido:.2f}")