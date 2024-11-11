"""
00 - faça um programa de média de duas notas de 1000 alunos,
mostrar as notas, a média, o nome do aluno e o status(
aprovado, reprovado e recuperação), sendo que para aprovação
o aluno precisa de uma nota acima ou igual a 7, reprovação
abaixo de 6 e recuperação acima/igual a 6 e menor que 7.

"""
cont = 0
quant = int(input("Informe a quantidade de alunos a serem avaliados: "))
while cont < quant:
    nome = input("Informe o nome: ")
    n1 = float(input("Informe a primeira nota: "))
    n2 = float(input("Informe a segunda nota: "))
    status = 0

    media = (n1+n2)/2
    if media >= 7:
        status = "Aprovado"
    elif media < 6:
        status = "Reprovado"
    else:
        status = "Recuperação"
    print(f"O nome {nome}, nota1 {n1}, nota2 {n2}, Media {media}, Status {status} ")

    cont +=1   #cont = cont + 1