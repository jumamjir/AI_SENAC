# 20. Gere um DataFrame com 10 colunas de valores aleatórios e use Matplotlib para
# exibir um gráfico de heatmap com a correlação entre as colunas.


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data20 = np.random.rand(10, 10)
df20 = pd.DataFrame(data20)

plt.imshow(df20.corr(), cmap='hot', interpolation='nearest')
plt.colorbar()
plt.title('Heatmap de Correlação')
plt.show()







