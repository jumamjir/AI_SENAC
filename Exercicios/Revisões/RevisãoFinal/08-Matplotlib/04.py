import matplotlib.pyplot as plt

cursos = ['Matemática', 'Física', 'Química', 'Biologia']
alunos = [30, 20, 25, 15]

plt.pie(alunos, labels=cursos, autopct='%1.1f%%', startangle=140)
plt.title('Distribuição de Alunos por Cursos')
plt.axis('equal')
plt.show()
