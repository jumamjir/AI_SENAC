import matplotlib.pyplot as plt
import numpy as np

meses = np.arange(1, 13)
temperatura = np.random.uniform(20, 30, 12)
precipitacao = np.random.uniform(0, 100, 12)

fig, ax1 = plt.subplots()

ax1.set_xlabel('Meses')
ax1.set_ylabel('Temperatura (°C)', color='tab:red')
ax1.plot(meses, temperatura, color='tab:red', label='Temperatura')
ax1.tick_params(axis='y', labelcolor='tab:red')

ax2 = ax1.twinx()
ax2.set_ylabel('Precipitação (mm)', color='tab:blue')
ax2.plot(meses, precipitacao, color='tab:blue', label='Precipitação')
ax2.tick_params(axis='y', labelcolor='tab:blue')

plt.title('Temperatura e Precipitação ao Longo do Ano')
plt.show()
