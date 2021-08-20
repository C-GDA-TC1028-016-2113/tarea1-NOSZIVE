def main():
    #escribe tu código abajo de esta línea
    #Autor Bryan Hernandez A01642287
    pesoinicial = float (input("Dame el peso inicial: "))
    pesofinal = float (input("Dame el peso final: "))
    meses = int(input("Dame la cantidad de meses: "))
    mes = (pesoinicial - pesofinal) / meses
    print("Lo que debes bajar por mes es:", mes)

    pass



if __name__ == '__main__':
    main()
