salario = float(input("Digite o valor do salário: "))
if salario < 2000:
    bonus = salario * 0.10
else:
    bonus = salario * 0.05
print(f"Bônus: R$ {bonus:.2f}")
