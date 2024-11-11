# 25. Crie um gráfico de barras usando os dados do DataFrame do exercício 11,
# mostrando as vendas totais por produto.

import pandas as pd
import matplotlib.pyplot as plt

dados = {
    'produto': ['A', 'B', 'C'],
    'quantidade': [10, 20, 30],
    'preco': [100, 150, 200]
}
df = pd.DataFrame(dados)

df['TotalV'] = df['quantidade'] * df['preco']

plt.bar(df['produto'], df['TotalV'], color='skyblue')

plt.title('Vendas Totais por Produto')
plt.xlabel('Produto')
plt.ylabel('Total de Vendas')

plt.show()
