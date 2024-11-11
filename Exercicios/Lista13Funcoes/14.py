# 14. Escreva uma função formata_data que receba uma data no formato dd/mm/aaaa
# e retorne a data no formato aaaa-mm-dd.

def formata_data(data):
    dia, mes, ano = data.split('/')
    return f"{ano}-{mes}-{dia}"

resultado = formata_data("25/12/2023")
print(resultado)
