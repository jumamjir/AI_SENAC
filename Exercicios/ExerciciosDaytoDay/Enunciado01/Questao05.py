#05-Controle de Fluxo) Fazer um programa que leia 2 valores e o tipo de media a ser calculada entre eles
# aritmética ou ponderada (1º 30% e 2º 70%)

num1 = int(input("Digite um valor:"))
num2 = int(input("Digite um valor:"))

mediAritmetica = (num1 + num2) / 2

mediaPonderada = ((num1 * 0.3) + (num2 * 0.7))

print(mediAritmetica)
print(mediaPonderada)



