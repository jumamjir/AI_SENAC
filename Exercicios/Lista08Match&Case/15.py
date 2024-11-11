# 15. Escreva um programa que solicite um tipo de conta (corrente, poupança, salário)
# e use match/case para exibir as características básicas de cada uma.

conta = input("Digite o tipo de conta (corrente, poupança, salário): ").strip().lower()

match conta:
    case "corrente":
        print("Conta corrente: Permite movimentação diária.")
    case "poupança":
        print("Conta poupança: Rendimento sobre o saldo.")
    case "salário":
        print("Conta salário: Para recebimento de salários.")
    case _:
        print("Tipo de conta não reconhecido.")
