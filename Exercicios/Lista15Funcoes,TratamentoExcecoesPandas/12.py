# 12. Faça uma função carregar_excel() que leia um arquivo Excel e retorne o
# DataFrame. Utilize tratamento de exceção para lidar com erros de leitura de
# arquivo e tipos de arquivo inválidos.

def carregar_excel(caminho):
    try:
        return pd.read_excel(caminho)
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
    except ValueError:
        print("Erro: Tipo de arquivo inválido.")
    except Exception as e:
        print(f"Erro: {e}")
