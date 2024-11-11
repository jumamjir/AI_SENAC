# 11. Escreva um programa que crie um dicionário com 5 países e suas capitais e
# permita que o usuário adicione novos pares de país-capital.


paises = {
    "Brasil": "Brasília",
    "França": "Paris",
    "Japão": "Tóquio",
    "Alemanha": "Berlim",
    "Canadá": "Ottawa"
}
while True:
    pais = input("Digite um país (ou 'sair' para encerrar): ")
    if pais.lower() == 'sair':
        break
    capital = input("Digite a capital do país: ")
    paises[pais] = capital
print(paises)
