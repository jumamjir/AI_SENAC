# 15. Faça uma função calcula_imc que receba o peso e a altura de uma pessoa e
# retorne o IMC.


def calcula_imc(peso,altura):
    return peso / (altura ** 2)


resultado = calcula_imc(80,1.78)
print(f"O IMC é: {resultado:.2f}") 