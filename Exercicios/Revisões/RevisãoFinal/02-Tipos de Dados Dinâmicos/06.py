data = input("Digite uma data no formato mm/dd/aaaa: ")
mes, dia, ano = data.split('/')
nova_data = f"{ano}{mes}-{dia}"
print(nova_data)
