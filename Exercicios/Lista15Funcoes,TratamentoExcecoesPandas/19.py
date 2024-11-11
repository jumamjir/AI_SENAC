# 19. Crie uma função converter_para_data() que receba um DataFrame e uma coluna,
# e converta os valores para o formato de data (datetime). Use tratamento de
# exceção para lidar com erros de conversão.

def converter_para_data(df, coluna):
    try:
        if coluna not in df.columns:
            raise ValueError(f"A coluna '{coluna}' não existe no DataFrame.")
        df[coluna] = pd.to_datetime(df[coluna])
        return df
    except Exception as e:
        print(f"Erro: {e}")
