# 05-Controle de Fluxo) Desenvolva um programa que permita ao usuário inserir uma quantidade definida de registros contendo
# nome, idade e estado civil. O estado civil deve ser escolhido entre 'casado', 'solteiro', 'divorciado' ou 'amasiado'.
# No final, exiba os dados inseridos e a quantidade total de pessoas em cada estado civil.


# nome = input("Digite seu nome:")
# idade = int(input("Digite sua idade:"))
# estado = int(input("Digite seu estado civil!Sendo 1 para casado, 2 para solteiro,3 para divorciado e 4 para amasiado:"))
#
#
# if estado == 1:
#     print(nome,"é casado!")
# elif estado == 2:
#     print(nome,"é solteiro!")
# elif estado == 3:
#     print(nome,"é divorciado!")
# elif estado ==4:
#     print(nome,"é amasiado!")

def main():
    estados_civis = {'casado': 0, 'solteiro': 0, 'divorciado': 0, 'amasiado': 0}
    registros = []

    quantidade = int(input("Digite a quantidade de registros que deseja inserir: "))

    for _ in range(quantidade):
        nome = input("Digite seu nome: ")
        idade = int(input("Digite sua idade: "))

        estado = int(input(
            "Digite seu estado civil! Sendo 1 para casado, 2 para solteiro, 3 para divorciado e 4 para amasiado: "))

        if estado == 1:
            estado_civil = 'casado'
            print(nome, "é casado!")
        elif estado == 2:
            estado_civil = 'solteiro'
            print(nome, "é solteiro!")
        elif estado == 3:
            estado_civil = 'divorciado'
            print(nome, "é divorciado!")
        elif estado == 4:
            estado_civil = 'amasiado'
            print(nome, "é amasiado!")
        else:
            print("Estado civil inválido. Tente novamente.")
            continue

        registros.append({'nome': nome, 'idade': idade, 'estado_civil': estado_civil})
        estados_civis[estado_civil] += 1

    print("\nRegistros inseridos:")
    for registro in registros:
        print(f"Nome: {registro['nome']}, Idade: {registro['idade']}, Estado Civil: {registro['estado_civil']}")

    print("\nQuantidade de pessoas em cada estado civil:")
    for estado, quantidade in estados_civis.items():
        print(f"{estado.capitalize()}: {quantidade}")


if __name__ == "__main__":
    main()
