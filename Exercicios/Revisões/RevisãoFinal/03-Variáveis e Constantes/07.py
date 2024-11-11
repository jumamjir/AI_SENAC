GRAVIDADE_TERRA = 9.8
GRAVIDADE_MARTE = 3.7
peso_terra = float(input("Digite o peso do objeto na Terra em kg: "))
peso_marte = peso_terra * (GRAVIDADE_MARTE / GRAVIDADE_TERRA)
print(f"Peso do objeto em Marte: {peso_marte:.2f} kg.")
