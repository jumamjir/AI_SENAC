dias_da_semana = ("Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado")
numero = int(input("Digite um número de 1 a 7: "))
if 1 <= numero <= 7:
    print(f"O dia correspondente é: {dias_da_semana[numero - 1]}")
else:
    print("Número inválido.")
