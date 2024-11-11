# 18. Crie um DataFrame com as vendas de diferentes categorias de produtos. Use
# Matplotlib para criar um gráfico de área empilhada para visualizar a evolução das
# vendas por categoria ao longo do tempo.


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data18 = np.random.randint(0, 100, size=(12, 4))
df18 = pd.DataFrame(data18, columns=['Categoria A', 'Categoria B', 'Categoria C', 'Categoria D'])

df18.plot(kind='area', stacked=True)
plt.title('Evolução das Vendas por Categoria')
plt.xlabel('Meses')
plt.ylabel('Vendas')
plt.show()




