# 6. Faça um programa que simule um caixa eletrônico. O usuário deve informar o
# valor a ser sacado. Utilize while para calcular o número de notas de 50, 20, 10 e 5
# necessárias. Use if para verificar a disponibilidade de notas.

def caixa_eletronico():
    notas = {
        50: 10,
        20: 10,
        10: 10,
        5: 10
    }

    valor_saque = int(input("Informe o valor a ser sacado: "))

    if valor_saque % 5 != 0:
        print("O valor deve ser múltiplo de 5.")
        return

    while valor_saque > 0:
        for nota in [50, 20, 10, 5]:
            if valor_saque >= nota and notas[nota] > 0:
                num_notas = valor_saque // nota
                if num_notas > notas[nota]:
                    num_notas = notas[nota]

                valor_saque -= num_notas * nota
                notas[nota] -= num_notas

                print(f'Total de notas de R${nota}: {num_notas}')

    print("Saque concluído!")


caixa_eletronico()
