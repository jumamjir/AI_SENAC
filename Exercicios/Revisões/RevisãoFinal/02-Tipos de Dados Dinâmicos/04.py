segundos = int(input("Digite um valor em segundos: "))
horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos_restantes = segundos % 60
print(f"{horas} horas, {minutos} minutos e {segundos_restantes} segundos.")
