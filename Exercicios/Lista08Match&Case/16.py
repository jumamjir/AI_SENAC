# 16. Crie um programa que solicite uma operação lógica (AND, OR, NOT) e dois valores
# booleanos; use match/case para realizar a operação.
operacao = input("Digite a operação lógica (AND, OR, NOT): ").strip().upper()
valor1 = input("Digite o primeiro valor booleano (True/False): ").strip().capitalize()
valor2 = input("Digite o segundo valor booleano (True/False): ").strip().capitalize()

bool1 = valor1 == "True"
bool2 = valor2 == "True"

match operacao:
    case "AND":
        resultado = bool1 and bool2
    case "OR":
        resultado = bool1 or bool2
    case "NOT":
        resultado = not bool1
        print(f"NOT {valor1} é: {resultado}")
        exit()
    case _:
        print("Operação inválida.")
        exit()

print(f"O resultado de {valor1} {operacao} {valor2} é: {resultado}")
