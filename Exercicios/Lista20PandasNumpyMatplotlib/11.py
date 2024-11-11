# 11. Crie um DataFrame com dados de vendas de três produtos ao longo de seis
# meses. Use 06-Pandas para calcular a média de vendas de cada produto e Matplotlib
# para exibir um gráfico de barras agrupadas.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data11 = np.random.randint(0, 100, size=(6, 3))
df11 = pd.DataFrame(data11, columns=['Produto A', 'Produto B', 'Produto C'])

media_vendas = df11.mean()
media_vendas.plot(kind='bar')
plt.title('Média de Vendas por Produto')
plt.xlabel('Produtos')
plt.ylabel('Média de Vendas')
plt.show()





