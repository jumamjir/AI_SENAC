# 2. Crie um programa que solicite uma nota entre 0 e 10. Caso a nota seja inválida,
# peça a entrada novamente usando while. Quando uma nota válida for inserida,
# exiba uma mensagem usando if para indicar se o aluno foi aprovado (nota ≥ 7) ou
# reprovado.

while True:
    num = int(input("Digite uma nota entre 0 e 10:"))
    if num < 0 or num >10:
        print("Digite uma nota válida!")
        continue
    elif num > 6:
        print("Você foi aprovado!")
    else:
        print("Você foi reprovado")
