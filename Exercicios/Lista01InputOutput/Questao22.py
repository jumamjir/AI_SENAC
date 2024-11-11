#22. Defina variáveis para as coordenadas de dois pontos e calcule a distância entre eles

from haversine import haversine

cristo_redentor = (22.9519, 43.2105)
paris = (48.8567, 2.3508)
latitude1 = cristo_redentor[0]
longitude1 = cristo_redentor[1]

latitude2 = paris[0]
longitude2 = paris[1]

print(f"Latitude: {latitude1}")
print(f"Longitude: {longitude1}")
print(f"Latitude: {latitude2}")
print(f"Longitude: {longitude2}")

distance = haversine(cristo_redentor, paris)
print("A distância entre Cristo Redentor e Paris é de aproximadamente:")
print(distance,"metros de distância")