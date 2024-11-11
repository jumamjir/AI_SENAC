# 9. Faça um jogo de adivinhação onde o usuário tem que adivinhar um número de 1 a
# 10. Use while para repetir as tentativas até que ele acerte. Utilize if para dar dicas
# se o número é maior ou menor.

import random

numero_secreto = random.randint(1, 10)
tentativa = 0

print("Adivinhe o número entre 1 e 10!")

while tentativa != numero_secreto:
    tentativa = int(input("Digite seu palpite: "))

    if tentativa < numero_secreto:
        print("O número é maior. Tente novamente!")
    elif tentativa > numero_secreto:
        print("O número é menor. Tente novamente!")
    else:
        print("Parabéns! Você acertou o número!")

print("Obrigado por jogar!")
