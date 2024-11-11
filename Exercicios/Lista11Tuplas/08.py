tupla1 = tuple(int(input("Digite 3 números para a primeira tupla: ")) for _ in range(3))
tupla2 = tuple(int(input("Digite 3 números para a segunda tupla: ")) for _ in range(3))
soma_tuplas = tuple(a + b for a, b in zip(tupla1, tupla2))
print("A nova tupla com a soma é:", soma_tuplas)
