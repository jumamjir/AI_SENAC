# 7. Crie um dicionário com 5 cidades e suas populações. Exiba a cidade com a maior
# população.

cidades = {
    "São Paulo": 12300000,
    "Rio de Janeiro": 6748000,
    "Belo Horizonte": 2527000,
    "Salvador": 2923000,
    "Fortaleza": 2687000
}
maior_populacao = max(cidades, key=cidades.get)
print(f"Cidade com maior população: {maior_populacao} ({cidades[maior_populacao]} habitantes)")
