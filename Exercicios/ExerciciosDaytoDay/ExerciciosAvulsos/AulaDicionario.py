dicPessoa = {}

for i in range(3):
    nome = input("Informe o nome:")
    idade = int(input("Informe a idade:"))
    identidade = int(input("Informe a identidade:"))
    dicPessoa[i] ={'Nome': nome, 'idade': idade, 'ident': identidade}


print(dicPessoa)

