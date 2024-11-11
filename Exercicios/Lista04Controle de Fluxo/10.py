# 10.Solicite ao usuário uma senha e verifique se ela está correta (use uma senha fixa
# para comparação).

senha = "123"

password = input("Digite a senha:")

if password != senha:
    print("Senha errada")
else:
    print("Senha correta")