def run():
#codigo
    soles = float(input("Ingresa la cantidad de soles que tienes: "))
    valor_dolar =3.80
    dolares = round((soles/valor_dolar),2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " Dolares")


if __name__=='__main__':
    run()