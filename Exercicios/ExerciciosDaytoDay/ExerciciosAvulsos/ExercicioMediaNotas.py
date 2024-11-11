#00- Faça um programa de média de duas notas de uma aluno,no final mostre as notas, nome do aluno e a média.

nomeAluno = input("Informe o nome do aluno: ")
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))

media = (nota1+nota2)/2

print("O nome: "+nomeAluno)
print("A nota 1: "+str(nota1))
print("A nota 2: "+str(nota2))
print("A Média: "+str(media))

print(f"O nome: {nomeAluno}, obteve nota1 {nota1}, nota2{nota2} com Média {media}")