limite_peso = 100
multa_por_kg = 4

peso_peixe = float(input("Informe o peso total: "))

if peso_peixe > limite_peso:
    excedente = peso_peixe - limite_peso
    multa = excedente * multa_por_kg

    print("Houveram",excedente,"kg de peixe a mais do permitido")
    print("O valo da multa é R$",multa)
else:
    print("Não foi o maior do que permitido")
print("Fora da identação")

