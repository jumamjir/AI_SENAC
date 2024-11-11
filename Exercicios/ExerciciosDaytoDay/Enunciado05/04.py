#4 – Faça um programa com dicionários que contenha os dados de várias pessoas.

dicPessoa = {}
for i in range(2):
    nome = input("Informe o nome:")
    idade = int(input("Informe a idade:"))
    identidade = int(input("Informe a identidade:"))
    altura = float(input("Informe a sua altura:"))

    dicPessoa[i] ={'Nome': nome,
                   'Idade': idade,
                   'Identidade': identidade,
                   'Altura': altura
                   }


print(dicPessoa)

