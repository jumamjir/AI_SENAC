#7-Faça um cadastro de uma empresa com os seguintes dados> razão social, nome fasntasia,cnpj
#endereco(logradouro),complemento,bairro,cep,cidade e Estado.Utilizar lista.

cadastro = []
razao = input("Digite a razão social:")
nomef = input("Digite o nome fantasia:")
cnpj = int(input("Digite o CPNJ:"))
endereco = input("Digite seu endereço:")
complemento = input("Digite o complemento:")
bairro = input("Digite o bairro:")
CEP = int(input("Digite o CEP:"))
UF = input("Digite o Estado:")
cidade = input("Digite a cidade:")


cadastro.append(razao)
cadastro.append(nomef)
cadastro.append(cnpj)
cadastro.append(endereco)
cadastro.append(complemento)
cadastro.append(bairro)
cadastro.append(CEP)
cadastro.append(UF)
cadastro.append(cidade)

print(cadastro)