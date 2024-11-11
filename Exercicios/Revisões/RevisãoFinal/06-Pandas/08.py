import pandas as pd

datas = pd.date_range(start='2023-01-01', periods=30)
valores = [i for i in range(30)]
df_series = pd.DataFrame({'Data': datas, 'Valor': valores})
df_series.set_index('Data', inplace=True)
media_7_dias = df_series['Valor'].resample('7D').mean()
print(media_7_dias)
