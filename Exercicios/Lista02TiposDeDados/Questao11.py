#11. Solicite uma lista de nomes e exiba o primeiro e o último nome da lista

lista = []
nome = input("Digite o nome : ")
lista.append(nome)
while nome:
    nome = input("Digite o nome : ")
    lista.append(nome)
    if nome == "exit":
        break
lista.pop()

print(lista[0])
print(lista[-1])