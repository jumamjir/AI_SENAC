# 19. Utilize 06-Pandas para ler um arquivo JSON com dados meteorológicos. Use NumPy
# para calcular a média da temperatura máxima e mínima e exiba um gráfico de
# barras comparando esses valores.


import pandas as pd
import matplotlib.pyplot as plt

df19 = pd.read_json('dados_meteorologicos.json')
media_maxima = df19['Temperatura Maxima'].mean()
media_minima = df19['Temperatura Minima'].mean()

plt.bar(['Maxima', 'Minima'], [media_maxima, media_minima])
plt.title('Temperaturas Médias')
plt.ylabel('Temperatura')
plt.show()











