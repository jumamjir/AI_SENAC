# 15. Faça uma função que leia um valor de um dicionário usando uma chave fornecida
# pelo usuário e trate exceções caso a chave não exista.

dic = {
    'chave1': 'valor1',
    'chave2': 'valor2',
    'chave3': 'valor3'
}

def ler_dic(chave):
    try:
        valor = dic[chave]
        print(f"O valor correspondente à chave '{chave}' é: {valor}")
    except KeyError:
        print("A chave não existe no dicionário.")

chave_usuario = input("Digite uma chave para ser inserida no dicionário: ")
ler_dic(chave_usuario)
