valor_hora = float(input("Digite o seu valor/hora: "))
qtd_horas = int(input("Digite quantas horas você trabalhou"))

ir = 0.11
inss = 0.08
sindicato = 0.05

salario_bruto = valor_hora * qtd_horas

valor_ir = salario_bruto * ir
valor_inss = salario_bruto * inss
valor_sindicato = salario_bruto* sindicato

salario_liquido = salario_bruto - valor_ir - valor_inss - valor_sindicato

print("Salario bruto:",salario_bruto)
print("Desconto IR:",valor_ir)
print("Desconto INSS:",valor_inss)
print("Desconto sindicato:",valor_sindicato)
print("Salário líquido:",salario_liquido)