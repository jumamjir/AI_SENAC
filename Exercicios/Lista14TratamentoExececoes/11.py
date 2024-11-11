# 11. Crie um programa que solicite uma data no formato dd/mm/aaaa e utilize
# tratamento de exceções para lidar com entradas incorretas de formato.

def validar_data(data):
    try:
        dia, mes, ano = map(int, data.split('/'))
        if not (1 <= dia <= 31 and 1 <= mes <= 12):
            raise ValueError("Dia ou mês fora do intervalo.")

        if mes == 2:
            if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
                if dia > 29:
                    raise ValueError("Fevereiro só tem 29 dias em anos bissextos.")
            else:
                if dia > 28:
                    raise ValueError("Fevereiro só tem 28 dias em anos não bissextos.")
        elif mes in [4, 6, 9, 11]:
            if dia > 30:
                raise ValueError("Esse mês só tem 30 dias.")

        print(f"A data {data} é válida.")
    except ValueError as e:
        print(f"Entrada inválida: {e}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


data = input("Digite uma data no formato dd/mm/aaaa: ")
validar_data(data)
