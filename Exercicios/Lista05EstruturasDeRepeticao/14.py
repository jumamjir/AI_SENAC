# 14.Solicite a idade de várias pessoas e calcule a média até que o usuário decida
# parar.

lista = []
while True:
    idade = int(input("Digite sua idade (ou 0 para sair):"))
    if idade == 0:
        break
    else:
        lista.append(idade)

soma = sum(lista)
divisao = soma / len(lista)
print("A média dos números:",divisao)
