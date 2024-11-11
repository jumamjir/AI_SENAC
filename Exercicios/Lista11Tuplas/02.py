tupla = tuple(int(input("Digite um número: ")) for _ in range(5))
numero = int(input("Digite um número para contar na tupla: "))
quantidade = tupla.count(numero)
print(f"O número {numero} aparece {quantidade} vezes na tupla.")
