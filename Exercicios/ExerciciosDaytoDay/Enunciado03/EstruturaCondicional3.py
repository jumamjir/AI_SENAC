#3 - Faça um programa que leia nome, idade, estado cívil e que será escolhido pelo usuário se é casado,
# solteiro,divorciado ou amasiado, será fornecido um número para cada opção e será mostrado somente o que escolheu.


nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))
estado = int(input("Digite seu estado civil!Sendo 1 para casado, 2 para solteiro,3 para divorciado e 4 para amasiado:"))


if estado == 1:
    print(nome,"é casado!")
elif estado == 2:
    print(nome,"é solteiro!")
elif estado == 3:
    print(nome,"é divorciado!")
elif estado ==4:
    print(nome,"é amasiado!")