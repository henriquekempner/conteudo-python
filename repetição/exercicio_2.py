nome = input("Digite o seu nome: ")
while len(nome) < 3:
    print("Nome inválido, ele precisa ter mais de 3 caracteres")
    nome = input("Digite o seu nome: ")

idade = int(input("Digite a sua idade: "))
while idade < 0 or idade > 150:
    print("Idade inválida, ela precisa ser entre 0 e 150 ")
    idade = int(input("Digite a sua idade:"))

salario = float(input("Digite o seu salário"))
while salario < 0:
    print("Salário inválido, ela precisa ser maior que 0")
    salario = float(input("Digite o seu salário: "))

es_civil = input("Digite o código do seu estado civil: ")
while es_civil != 's' and es_civil != 'c' and es_civil != "v" and es_civil != 'd':
    print("Valor inválido, digite conforme os códigos")
    es_civil = input("Digite o código do seu estado civil: ")

