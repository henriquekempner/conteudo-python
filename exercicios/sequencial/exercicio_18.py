tamanho_arquivo = float(input("Informe o tamanho do aquivo (em MB): "))
velocidade_internet = float(input("Informe a velocidade da internet (em Mbps): "))

tamanho_megabites = tamanho_arquivo * 8

tempo_segundos = tamanho_megabites / velocidade_internet

tempo_minutos = tempo_segundos / 60

print(f"O tempo aproximado de download é de {tempo_minutos:.2f} minutos.")