# 30. Gere um DataFrame com dados aleatórios de temperatura e precipitação e exiba
# gráficos de linha duplos com dois eixos y (um para temperatura e outro para
# precipitação).


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data30 = {
    'Mes': np.arange(1, 13),
    'Temperatura': np.random.rand(12) * 30,
    'Precipitacao': np.random.rand(12) * 100
}
df30 = pd.DataFrame(data30)

fig, ax1 = plt.subplots()

ax1.set_xlabel('Mês')
ax1.set_ylabel('Temperatura', color='tab:red')
ax1.plot(df30['Mes'], df30['Temperatura'], color='tab:red', label='Temperatura')
ax1.tick_params(axis='y', labelcolor='tab:red')

ax2 = ax1.twinx()
ax2.set_ylabel('Precipitação', color='tab:blue')
ax2.plot(df30['Mes'], df30['Precipitacao'], color='tab:blue', label='Precipitação')
ax2.tick_params(axis='y', labelcolor='tab:blue')

plt.title('Temperatura e Precipitação ao Longo do Ano')
plt.show()
















