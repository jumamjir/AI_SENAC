# 28. Calcule o seno e cosseno de um array de ângulos em radianos (0 a π) e exiba os
# resultados.


import numpy as np

angulos = np.linspace(0, np.pi, 5)  # 5 ângulos entre 0 e π

seno = np.sin(angulos)
cosseno = np.cos(angulos)

print("Ângulos:", angulos)
print("Seno:", seno)
print("Cosseno:", cosseno)