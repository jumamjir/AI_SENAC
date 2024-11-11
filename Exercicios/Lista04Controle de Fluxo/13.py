# 13.Leia a temperatura e exiba se está frio (abaixo de 15°C), ameno (15 a 25°C) ou
# quente (acima de 25°C).

temperatura = float(input("Digite a temperatura em ºC: "))
if temperatura < 15.0:
    print("Está frio")
elif temperatura >= 15 and temperatura < 26:
    print("Está ameno")
else:
    print("Está quente")

