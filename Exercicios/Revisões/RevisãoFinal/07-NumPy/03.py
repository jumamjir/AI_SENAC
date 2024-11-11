import numpy as np

array = np.random.rand(100)
media = np.mean(array)
desvio_padrao = np.std(array)
array_normalizado = (array - media) / desvio_padrao
print(array_normalizado)
