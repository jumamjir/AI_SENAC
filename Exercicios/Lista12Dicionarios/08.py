# 8. Escreva um programa que crie um dicionário com os dados de um funcionário
# (nome, cargo, salário) e permita ao usuário atualizar o salário.

funcionario = {
    "nome": "Carlos",
    "cargo": "Desenvolvedor",
    "salario": 5000.00
}
novo_salario = float(input("Digite o novo salário: "))
funcionario["salario"] = novo_salario
print(funcionario)
