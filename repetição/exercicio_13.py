valor = int(input("Digite o valor: "))

contador = valor
resultado = 1
while contador>0:
    resultado = resultado * contador
    contador = contador - 1

print(f"O fatorial de {valor} é {resultado}")