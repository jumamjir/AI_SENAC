# 16. Gere um DataFrame com 100 valores aleatórios entre 1 e 10 e exiba um gráfico de
# densidade (KDE) desses valores usando Matplotlib.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data16 = np.random.randint(1, 11, size=100)
df16 = pd.DataFrame(data16, columns=['Valores'])

df16.plot(kind='kde')
plt.title('Gráfico de Densidade')
plt.xlabel('Valores')
plt.ylabel('Densidade')
plt.show()






