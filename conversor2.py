def run():

    menu="""
    Bienvenido al conversor de monedas 
    1 - soles
    2 - Pesos colombianos
    3 - Pesos argentinos
    4 - Pesos mexicanos
    """
    print(menu)
    opcion=int(input("Elige una opción: "))
    monto=float(input("Ingrese el monto a convertir a dolares: "))

    if opcion == 1:
        resultado=float(monto/3.80)
        print("Tienes",(round(resultado,2)),"dolares americanos")
    elif opcion ==2:
        resultado=float(monto/3875)
        print("Tienes",(round(resultado,2)),"dolares americanos")
    elif opcion ==3:
        resultado=float(monto/65)
        print("Tienes",(round(resultado,2)),"dolares americanos")
    elif opcion ==4:
        resultado=float(monto/24)
        print("Tienes",(round(resultado,2)),"dolares americanos")
    else:
        print("Ingresa una opcion correcta")


if __name__=='__main__':
    run()