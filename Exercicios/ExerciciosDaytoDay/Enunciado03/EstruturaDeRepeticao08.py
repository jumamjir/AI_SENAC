def calcular_salario(horas_trabalhadas, salario_hora):
    return horas_trabalhadas * salario_hora

def calcular_descontos(salario_bruto, percentual_desconto):
    return salario_bruto * percentual_desconto / 100

def calcular_salario_liquido(salario_bruto, descontos):
    return salario_bruto - descontos

def main():
    funcionarios = []
    num_funcionarios = int(input("Quantos funcionários você deseja cadastrar? "))

    for _ in range(num_funcionarios):
        nome = input("\nDigite o nome do funcionário: ")
        salario_hora = float(input("Digite o salário por hora: R$ "))
        horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))
        percentual_desconto = float(input("Digite o percentual de descontos (ex: 10 para 10%): "))

        salario_bruto = calcular_salario(horas_trabalhadas, salario_hora)
        descontos = calcular_descontos(salario_bruto, percentual_desconto)
        salario_liquido = calcular_salario_liquido(salario_bruto, descontos)

        funcionarios.append({
            'nome': nome,
            'salario_bruto': salario_bruto,
            'descontos': descontos,
            'salario_liquido': salario_liquido
        })

    print("\nFolha de Pagamento:")
    for func in funcionarios:
        print(f"\nNome: {func['nome']}")
        print(f"Salário Bruto: R$ {func['salario_bruto']:.2f}")
        print(f"Descontos: R$ {func['descontos']:.2f}")
        print(f"Salário Líquido: R$ {func['salario_liquido']:.2f}")

    # Calcular e mostrar totais
    total_salario_bruto = sum(func['salario_bruto'] for func in funcionarios)
    total_descontos = sum(func['descontos'] for func in funcionarios)
    total_salario_liquido = sum(func['salario_liquido'] for func in funcionarios)

    print("\nResumo da Folha de Pagamento:")
    print(f"Total de Salário Bruto: R$ {total_salario_bruto:.2f}")
    print(f"Total de Descontos: R$ {total_descontos:.2f}")
    print(f"Total de Salário Líquido: R$ {total_salario_liquido:.2f}")

if __name__ == "__main__":
    main()
