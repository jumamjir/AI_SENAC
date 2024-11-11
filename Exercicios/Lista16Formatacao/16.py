def calcular_juros(valor, taxa, periodo):
    valor_final = valor * ((1 + taxa) ** periodo)
    return valor_final
