idade = int(input("Digite a idade da pessoa: "))
if idade <= 12:
    print("Criança")
elif 13 <= idade <= 17:
    print("Adolescente")
elif 18 <= idade <= 64:
    print("Adulta")
else:
    print("Idosa")
