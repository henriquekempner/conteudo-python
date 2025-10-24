litros = float(input("Quantas litros você quer abastecer?"))
combustivel = input("Qual é o combustivel que você quer? (G - Gasolina, A - Alcool): ")

match combustivel:
    case "A":
        #Alcool
        if litros > 20:
            pct_desconto = 5
        else:
            pct_desconto = 3

        val_total = litros * 4.17
        val_desconto = val_total * (pct_desconto/100)
        val_liquido = val_total - val_desconto

        print(f"Você vai pagar R${val_liquido}")
        print(f"Você teve {pct_desconto}% de desconto, economizado R${val_desconto}")

    case "G":
        #Gasolina
        if litros > 20:
            pct_desconto = 6
        else:
            pct_desconto = 4

        val_total = litros * 6.29
        val_desconto = val_total * (pct_desconto / 100)
        val_liquido = val_total - val_desconto

print(f"Você vai pagar R${val_liquido}")
print(f"Você teve {pct_desconto}% de desconto, economizado R${val_desconto}")