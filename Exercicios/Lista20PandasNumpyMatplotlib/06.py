# 6. Crie um DataFrame com dados fictícios de notas de alunos em três disciplinas.
# Calcule a média das notas por aluno e exiba um gráfico de barras empilhadas com
# as notas das disciplinas.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data6 = np.random.rand(10, 3) * 10
df6 = pd.DataFrame(data6, columns=['Matemática', 'Português', 'Inglês'])
media_alunos = df6.mean(axis=1)

df6.plot(kind='bar', stacked=True)
plt.title('Notas dos Alunos por Disciplina')
plt.xlabel('Alunos')
plt.ylabel('Notas')
plt.show()





