# 9. Utilize NumPy para calcular a média, mediana e desvio padrão de um array de
# números aleatórios.

import numpy as np


a = np.random.randint(10)

media = np.mean(a)


mediana = np.median(a)


desvio_padrao = np.std(a)


print("Média:", media)
print("Mediana:", mediana)
print("Desvio padrão:", desvio_padrao)