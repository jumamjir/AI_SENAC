# 13. Escreva uma função que solicite uma senha e compare com uma senha fixa.
# Capture exceções caso a senha não atenda aos requisitos mínimos de tamanho.


def senha():
    try:
        psw = input("Digite sua senha: ")
        senhaFixa = 'joaozin123'

        if len(psw) < len(senhaFixa):
            raise ValueError("A senha deve ter pelo menos {} caracteres.".format(len(senhaFixa)))

        if psw != senhaFixa:
            print("Senha Inválida")
        else:
            print("Senha válida!")

    except ValueError as e:
        print("Erro:", e)


senha()

