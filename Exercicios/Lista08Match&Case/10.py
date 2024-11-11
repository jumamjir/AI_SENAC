# 10. Solicite ao usuário um tipo de transporte (carro, moto, bicicleta, ônibus) e use
# match/case para exibir a quantidade de rodas.

transporte = input("Digite um tipo de transporte (carro, moto, bicicleta, ônibus): ").strip().lower()

match transporte:
    case "carro":
        print("Um carro geralmente tem 4 rodas.")
    case "moto":
        print("Uma moto geralmente tem 2 rodas.")
    case "bicicleta":
        print("Uma bicicleta geralmente tem 2 rodas.")
    case "ônibus":
        print("Um ônibus geralmente tem 6 rodas.")
    case _:
        print("Transporte inválido. Por favor, digite carro, moto, bicicleta ou ônibus.")
