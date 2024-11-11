# 15. Solicite dois valores booleanos e exiba o resultado das operações and, or e not.


booleano = int(input("Digite 1 para True e 0 para False:"))
booleano2 = int(input("Digite 1 para True e 0 para False:"))

if booleano == 0:
    print("O valor do primeiro Booleano é: ", False)
else:
    print("O valor do primeiro Booleano é: ", True)

if booleano == 0:
    print("O valor do primeiro Booleano é: ", False)
else:
    print("O valor do primeiro Booleano é: ", True)

# booleano = True
# booleano2 = False

if (booleano and booleano2) == True:
    print("Como ambos são True, o resultado é:", True)
else:
    print("Como um dos dois não é True, o resultado é:", False)

if (booleano or booleano2) == True:
    print("Como um ou outro é True o, resultado é:", True)
else:
    print("Como nenhum dos dois é True, o resultado é:", False)

if (not booleano) == False:
    print("Como a negação de um valor True é false ,o resultado é:", False)
else:
    print("Como a negação de um valor False é True ,o resultado é:", True)

if (not booleano2) == False:
    print("Como a negação de um valor True é False ,o resultado é:", False)
else:
    print("Como a negação de um valor False é True ,o resultado é:", True)