import matplotlib.pyplot as plt
import numpy as np

vendedores = ['Alice', 'Bob', 'Carlos', 'Daniel']
pontuacoes = [88, 95, 80, 90]

plt.barh(vendedores, pontuacoes, color='skyblue')
plt.title('Desempenho dos Vendedores')
plt.xlabel('Pontuação')
plt.ylabel('Vendedores')

maior_vendedor = np.argmax(pontuacoes)
plt.barh(vendedores[maior_vendedor], pontuacoes[maior_vendedor], color='orange')
plt.show()
