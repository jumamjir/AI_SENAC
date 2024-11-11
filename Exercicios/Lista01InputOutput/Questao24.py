#24. Solicite o salário de um funcionário e use uma constante de bônus para calcular o salário total.

salario = float(input("Digite seu salário mensal:"))
bonus = 0.2
salarioTotal = (salario * bonus) + salario

print("O seu salário mais o bonus será igual a:$",salarioTotal)