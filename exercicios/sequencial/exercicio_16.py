import math

area = float(input("Informe a área a ser pintada: "))

cob_por_metro = 3
qtd_tinta_lata = 18
valor_lata = 80.0

litros_necessarios = area / cob_por_metro
print("São necessários",litros_necessarios,"l de tinta")

qtd_latas = litros_necessarios / qtd_tinta_lata
print("São necessários",qtd_latas,"latas de tinta")

print("### Com valor exato ###")
valor = qtd_latas * valor_lata
print("O valor necessário da tinta, é R$",round(valor,2))

print("### Com quantidades inteiras de latas ###")
qtd_latas = math.ceil(qtd_latas)
print("São necessários",qtd_latas,"latas de tinta")
valor = qtd_latas * valor_lata
print("O valor necessário da tinta, é R$",valor)