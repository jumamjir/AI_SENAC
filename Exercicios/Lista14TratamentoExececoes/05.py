# 5. Crie uma função que solicite um número do usuário e calcule a raiz quadrada. Use
# tratamento de exceções para lidar com números negativos.


def raiz_quadrada():
    try:
        r = float(input("Digite um número que deseja saber a raiz: "))
        if r < 0:
            raise ValueError("Número negativo!")
        raiz = r ** (1/2)
        print(f"A raiz quadrada de {r} é: {raiz}")
    except ValueError as e:
        print(e)

raiz_quadrada()
