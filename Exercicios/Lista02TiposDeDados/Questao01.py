#1. Leia uma string, um inteiro, um float e um booleano do usuário e exiba os tipos de dados lidos.

string = input("Digite uma frase:")
inteiro = int(input("Digite um número inteiro:"))
quebrado = float(input("Digite um número com casas decimais:"))
serOuNaoSer = bool(input("Digite '1' ou '0' :"))



print(type(string))
print(type(inteiro))
print(type(quebrado))
print(type(serOuNaoSer))
