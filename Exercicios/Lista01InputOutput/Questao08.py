#8. Solicite um número e exiba o seu quadrado e sua raiz quadrada.

num1 = int(input("Digite um número:"))

aoQuadrado = (num1 * num1)
#raizQuadrada = (aoQuadrado / num)

print(num1,"ao quadrado é igual a:",aoQuadrado)
#print("A raiz quadrada de",aoQuadrado,"é igual a:",raizQuadrada)
num = int(input("Digite o número de que se deseja saber a raiz quadrada:"))

def raizQuadrada(num, num_interacoes=100):
    adivinha = num
    for _ in range(num_interacoes):
        adivinha = (adivinha + num / adivinha) / 2
    return adivinha

resultado = raizQuadrada(num)
print(f"A raiz quadrada de {num} é aproximadamente:{resultado}")



