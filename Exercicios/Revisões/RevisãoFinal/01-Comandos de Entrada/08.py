def converter_horas_para_dias(horas):
    dias = horas // 24
    horas_restantes = horas % 24
    return dias, horas_restantes

horas = int(input("Digite a quantidade de horas: "))
dias, horas_restantes = converter_horas_para_dias(horas)
print(f"{horas} horas equivalem a {dias} dias e {horas_restantes} horas.")
