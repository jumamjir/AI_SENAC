import math

ponto1 = (float(input("Digite a coordenada x1: ")), float(input("Digite a coordenada y1: ")))
ponto2 = (float(input("Digite a coordenada x2: ")), float(input("Digite a coordenada y2: ")))

distancia = math.sqrt((ponto2[0] - ponto1[0])**2 + (ponto2[1] - ponto1[1])**2)
print("A distância entre os pontos é:", distancia)
