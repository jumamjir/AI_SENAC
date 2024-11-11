GRAVIDADE_TERRA = 9.8
t = float(input("Digite o tempo em segundos: "))
velocidade = GRAVIDADE_TERRA * t
print(f"A velocidade após {t} segundos é: {velocidade:.2f} m/s.")
