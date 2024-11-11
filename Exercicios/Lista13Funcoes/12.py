# 12. Faça uma função hipotenusa que receba os dois catetos de um triângulo
# retângulo e retorne a hipotenusa.



def hipotenusa(cateto1,cateto2):
    hip = cateto1**2 + cateto2**2
    return hip ** (1/2)

resultado = hipotenusa(3,5)
print(f"O resultado é {resultado:.2f}")