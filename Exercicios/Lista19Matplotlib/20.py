# 20. Desenhe um gráfico de barras empilhadas com três séries de dados,
# representando as vendas trimestrais de três produtos. Utilize cores diferentes para
# cada série.

import matplotlib.pyplot as plt
import numpy as np

meses = ['Janeiro', 'Fevereiro', 'Março']
produto1 = np.array([3, 4, 5])
produto2 = np.array([2, 3, 4])
produto3 = np.array([2, 5, 4])

plt.bar(meses, produto1, color='blue', label='Produto 1')
plt.bar(meses, produto2, bottom=produto1, color='red', label='Produto 2')
plt.bar(meses, produto3, bottom=produto1 + produto2, color='green', label='Produto 3')

plt.xlabel('Meses')
plt.ylabel('Vendas')

plt.legend()
plt.show()
