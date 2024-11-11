# 7.Solicite um ano e verifique se ele é bissexto.

ano = int(input("Digite um ano:"))

if ano % 4 ==0:
    print("Ano bissexto")
else:
    print("Ano normal")