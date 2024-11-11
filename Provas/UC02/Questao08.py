# 8-Faça uma lista com nomes de frutas e com uma fruta informada pelo usuário,
# verificar se há esta fruta na lista.


frutas = ['maça', 'banana', 'uva']
fruit = input("Digite uma fruta:")

if fruit in frutas:
    print("A fruta já está na lista. Digite outra fruta.")
else:
    frutas.append(fruit)
    print("Fruta adicionada com sucesso.")

print(frutas)
