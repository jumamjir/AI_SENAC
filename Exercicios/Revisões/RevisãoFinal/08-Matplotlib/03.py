import matplotlib.pyplot as plt
import numpy as np

produtos = ['Produto A', 'Produto B', 'Produto C']
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril']
vendas = np.array([[20, 35, 30, 35], [25, 32, 34, 20], [30, 22, 30, 25]])

x = np.arange(len(meses))
largura = 0.2

for i in range(len(produtos)):
    plt.bar(x + i * largura, vendas[i], largura, label=produtos[i])

plt.xlabel('Meses')
plt.ylabel('Vendas')
plt.title('Vendas de Produtos por Mês')
plt.xticks(x + largura, meses)
plt.legend()
plt.show()
