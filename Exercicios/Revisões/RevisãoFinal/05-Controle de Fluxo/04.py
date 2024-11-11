temperatura = float(input("Digite a temperatura do ambiente: "))
if temperatura < 20:
    print("A temperatura está abaixo da faixa de conforto.")
elif 20 <= temperatura <= 25:
    print("A temperatura está dentro da faixa de conforto.")
else:
    print("A temperatura está acima da faixa de conforto.")
