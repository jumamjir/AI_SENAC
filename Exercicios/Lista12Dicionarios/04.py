# 4. Crie um dicionário com nomes e idades de 5 pessoas e exiba a idade de uma
# pessoa fornecida pelo usuário.

pessoas = {
    "Ana": 25,
    "Pedro": 30,
    "Lucas": 22,
    "Maria": 28,
    "Carla": 35
}
nome = input("Digite o nome da pessoa: ")
idade = pessoas.get(nome, "Pessoa não encontrada.")
print(f"Idade de {nome}: {idade}")
