# 6 - Faça um programa com nome, idade e sexo de 20 pessoas. Mostrar somente o nome se a pessoa for sexo feminino e tiver mais que 18 anos,
# mostrar qual o nome,sexo e idade de todos, e no final mostrar:
# - Mostrar a média de idades de todos
# - Mostrar a média de idades das mulheres
# - Mostrar a média de idades não mulheres
# - Mostrar a maior média das mulheres e o nome
# - Mostrar a menor média das mulheres e o nome
# - Mostrar a maior média das não mulheres e o nome
# - Mostrar a menor média das não mulheres e o nome
# - A maior idade de todos e o nome
# - A menor idade de todos e o nome
# - A maior idade das mulheres e o nome
# - A menor idade das mulheres e o nome
# - A maior idade de não mulheres e o nome
# - A menor idade de não mulheres e o nome

# Listas para armazenar informações
nomes = []
idades = []
sexos = []

# Coleta de dados de 20 pessoas
for _ in range(20):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    sexo = input("Digite seu sexo (M/F): ").upper()

    nomes.append(nome)
    idades.append(idade)
    sexos.append(sexo)

# Cálculo da média de idades
total_idade = sum(idades)
media_idade = total_idade / len(idades)

# Filtrando idades por sexo
idades_mulheres = [idades[i] for i in range(len(sexos)) if sexos[i] == 'F']
idades_nao_mulheres = [idades[i] for i in range(len(sexos)) if sexos[i] != 'F']

media_idade_mulheres = sum(idades_mulheres) / len(idades_mulheres) if idades_mulheres else 0
media_idade_nao_mulheres = sum(idades_nao_mulheres) / len(idades_nao_mulheres) if idades_nao_mulheres else 0

# Encontrar a maior e menor idade de todos, mulheres e não mulheres
maior_idade = max(idades)
menor_idade = min(idades)

maior_idade_mulheres = max(idades_mulheres) if idades_mulheres else None
menor_idade_mulheres = min(idades_mulheres) if idades_mulheres else None

maior_idade_nao_mulheres = max(idades_nao_mulheres) if idades_nao_mulheres else None
menor_idade_nao_mulheres = min(idades_nao_mulheres) if idades_nao_mulheres else None

# Encontrar nomes associados às maiores e menores idades
nome_maior_idade = nomes[idades.index(maior_idade)]
nome_menor_idade = nomes[idades.index(menor_idade)]

nome_maior_idade_mulheres = nomes[idades_mulheres.index(maior_idade_mulheres)] if maior_idade_mulheres else None
nome_menor_idade_mulheres = nomes[idades_mulheres.index(menor_idade_mulheres)] if menor_idade_mulheres else None

nome_maior_idade_nao_mulheres = nomes[
    idades_nao_mulheres.index(maior_idade_nao_mulheres)] if maior_idade_nao_mulheres else None
nome_menor_idade_nao_mulheres = nomes[
    idades_nao_mulheres.index(menor_idade_nao_mulheres)] if menor_idade_nao_mulheres else None

# Exibindo resultados
print("\nInformações coletadas:")
for i in range(20):
    print(f"Nome: {nomes[i]}, Idade: {idades[i]}, Sexo: {sexos[i]}")

print(f"\nMédia de idades de todos: {media_idade:.2f}")
print(f"Média de idades das mulheres: {media_idade_mulheres:.2f}")
print(f"Média de idades não mulheres: {media_idade_nao_mulheres:.2f}")

print(f"\nMaior idade de todos: {maior_idade} (Nome: {nome_maior_idade})")
print(f"Menor idade de todos: {menor_idade} (Nome: {nome_menor_idade})")

print(f"\nMaior idade das mulheres: {maior_idade_mulheres} (Nome: {nome_maior_idade_mulheres})")
print(f"Menor idade das mulheres: {menor_idade_mulheres} (Nome: {nome_menor_idade_mulheres})")

print(f"\nMaior idade das não mulheres: {maior_idade_nao_mulheres} (Nome: {nome_maior_idade_nao_mulheres})")
print(f"Menor idade das não mulheres: {menor_idade_nao_mulheres} (Nome: {nome_menor_idade_nao_mulheres})")


