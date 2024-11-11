import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array(range(10)).reshape(-1, 1)
y = np.array([1, 2, 3, 4, 5, 6, 8, 7, 9, 10]) + np.random.normal(0, 1, 10)

plt.scatter(x, y)
modelo = LinearRegression().fit(x, y)
y_pred = modelo.predict(x)
plt.plot(x, y_pred, color='red', label='Linha de Tendência')
plt.title('Gráfico de Linhas com Linha de Tendência')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
