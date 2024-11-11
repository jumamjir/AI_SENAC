# #14. Leia um número binário (em string) e exiba seu valor em decimal.
#
# # 69 1000101
#
# numBinario = input("Digite um número binário: ")
#
# def binaryToDecimal(str):
#     dec_num = 0
#     power = 0
#     n = len(str)
#
#     # Iterate through the string str
#     for i in range(n - 1, -1, -1):
#         if (str[i] == '1'):
#             dec_num += (2 ** power)
#         power += 1
#
#     return dec_num
#
# print(binaryToDecimal(numBinario))


def binary_to_decimal(binary_str):
    return int(binary_str,2)

num_binario = input("Digite um número binário: ")

print(binary_to_decimal(num_binario))