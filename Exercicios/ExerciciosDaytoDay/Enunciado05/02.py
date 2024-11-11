#2 - Faça um programa com dicionários com de veículos e suas marcas


dicionario = {}
for i in range(3):
    veiculo = input("Digite o nome de um veículo:")
    marca = input("Digite a marca desse veículo:")
    dicionario[i] = {'Veiculo': veiculo,
                     'Marca': marca}


print(dicionario)