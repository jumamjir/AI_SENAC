# 10. Crie um gráfico de barras empilhadas para comparar as vendas de dois produtos
# ao longo de três meses (Produto 1: [3, 4, 5], Produto 2: [2, 3, 4]).

import matplotlib.pyplot as plt

meses = ['Janeiro','Fevereiro','Março']
produto1 = [3, 4, 5]
produto2 = [2, 3, 4]


plt.bar(meses,produto1, color='blue',label='Produto 1')

plt.bar(meses,produto2,bottom=produto1, color='red',label='Produto 2')

plt.xlabel('Meses')
plt.ylabel('Vendas')
plt.title('Vendas ao longo de 3 Meses')

plt.legend()
plt.show()
