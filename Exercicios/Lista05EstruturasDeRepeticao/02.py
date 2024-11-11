# 2.Solicite um número do usuário e exiba sua tabuada do 1 ao 10.

num = int(input("Digite um número:"))

for i in range (1,11):
    resultado = num * i
    print(f"O resultado vezes {i} :",resultado)