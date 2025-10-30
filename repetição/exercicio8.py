num1 = int(input("Insira o primeiro numero: "))
num2 = int(input("Insira o segundo numero"))

soma = 0

for numero in range(num1+1,num2):
    print(numero)
    soma = soma + numero

print(f"A soma é {soma}")