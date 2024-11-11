import matplotlib.pyplot as plt
import numpy as np

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril']
vendas_A = [200, 300, 250, 400]
vendas_B = [150, 220, 270, 350]

plt.fill_between(meses, vendas_A, color="skyblue", alpha=0.4)
plt.fill_between(meses, vendas_B, color="orange", alpha=0.4)
plt.title('Distribuição Acumulada de Vendas')
plt.xlabel('Meses')
plt.ylabel('Vendas')
plt.legend(['Produto A', 'Produto B'])
plt.show()
