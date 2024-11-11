# 2. Escreva um programa que crie um dicionário com os meses do ano e o número de
# dias em cada mês. Exiba o número de dias de um mês fornecido pelo usuário.

meses = {
    "Janeiro": 31,
    "Fevereiro": 28,
    "Março": 31,
    "Abril": 30,
    "Maio": 31,
    "Junho": 30,
    "Julho": 31,
    "Agosto": 31,
    "Setembro": 30,
    "Outubro": 31,
    "Novembro": 30,
    "Dezembro": 31
}
mes = input("Digite o nome do mês: ")
print(f"Número de dias em {mes}: {meses.get(mes, 'Mês inválido')}")
