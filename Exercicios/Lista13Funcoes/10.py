# 10. Crie uma função fahrenheit_para_celsius que converta uma temperatura de
# Fahrenheit para Celsius. Receba a temperatura em Fahrenheit como parâmetro.


def fahrenheit_para_celsius(temp):
    return ((temp - 32) * 5) / 9


resultado = (fahrenheit_para_celsius(10))
print(f"{resultado:.2f}") 