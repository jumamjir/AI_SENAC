#5-Faça a soma dos números pares e ímpares entre -234 e 8644.

pares = []
impares = []

for i in range(-234, 8645):
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

soma_pares =sum(pares)
soma_impares =sum(impares)
print(soma_pares + soma_impares)