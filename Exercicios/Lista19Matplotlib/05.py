# 5. Crie um gráfico de pizza com as porcentagens de vendas de 4 produtos (A = 30%,
# B = 25%, C = 20%, D = 25%). Adicione rótulos e destaque o produto A.

import matplotlib.pyplot as plt


produtos = ['A','B','C','D']
valores = [30,25,20,25]
explode = (0.1, 0, 0, 0)

plt.pie(valores, labels=produtos, autopct='%1.1f%%', explode=explode, startangle=90)

plt.show()
