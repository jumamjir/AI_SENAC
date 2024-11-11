# #12. Leia um texto e exiba apenas os números presentes no texto, se houver.


textao = input("Digite um textão:")

print("A string original é : " + textao)

nums = [int(i) for i in textao.split() if i.isdigit()]

print("Os números desse texto são :" + str(nums))