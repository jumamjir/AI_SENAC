import pandas as pd


dados= [1,2,3,4,5,6,7,8,9,10]

df = pd.DataFrame({'numeros': dados})
print(df)

media = df['numeros'].mean()
mediana = df['numeros'].median()
desvioP = df['numeros'].std()

print(f"Média: {media}, Mediana: {mediana}, e Desvio Padrão: {desvioP:.2f}")
