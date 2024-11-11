continuar = 0
lnome=[]
lidade=[]
lcpf=[]

while continuar == 0:
    lnome.append(input("Informe o nome: "))
    lidade.append(int(input("Informe a idade: ")))
    lcpf.append(int(input("Informe o cpf: ")))
    continuar = int(input("informe zero para continuar"))

tam = len(lnome)
i=0
while i < tam: # também pode len(lnome) substituindo o tam
   print(f"Nome: {lnome[i]}, Idade: {lidade[i]}, CPF: {lcpf[i]}")
   i+=1