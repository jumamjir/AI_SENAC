# 3-Faça um programa para calcular a média aritmética de alturas de um grupo de 8 pessoas,
# para cada uma delas verifique se tem a alura menor que 1,6 m mostrar mensagem de estatura baixa,
# maior que 2,0 m mensagem de estatura alta, entre estes dois valores estatura mediana. Também mostrar
# o nome de cada uma delas, a altura e a mensagem da estatura , não usar lista.

for i in range(8):
    altura = float(input("Digite sua altura:"))
    nome = input("Digite seu nome:")
    if altura < 1.6:
        print("Estatura baixa.")
    elif altura > 2.0:
        print("Estatura alta.")
    else:
        print("Estatura mediana.")
    print(nome)

