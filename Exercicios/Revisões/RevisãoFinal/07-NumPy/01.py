import numpy as np

array = np.random.randint(0, 51, size=20)
multiplos_de_5 = array[array % 5 == 0]
print(multiplos_de_5)
