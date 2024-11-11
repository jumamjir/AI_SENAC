# 25. Crie uma função palindromo que receba uma string e retorne True se for um
# palíndromo, e False caso contrário.

def palindromo(frase):
    if (frase[::-1]) == frase:
        return True
    else:
        return False

resul = palindromo('luzazul')
print(resul)