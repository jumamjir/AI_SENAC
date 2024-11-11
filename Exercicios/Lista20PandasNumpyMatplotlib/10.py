# 10. Utilize NumPy para gerar um array com os valores de seno de 0 a 2π. Crie um
# DataFrame com esses valores e exiba um gráfico de linha do seno usando
# Matplotlib.


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
seno = np.sin(x)
df10 = pd.DataFrame(seno, columns=['Seno'])

plt.plot(x, df10['Seno'])
plt.title('Gráfico do Seno')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.show()



