def run():
    nombre=input("Ingresa tu nombre: ")
    apellido=input("Ingresa tu apellido: ")
    for i in nombre.upper():
        for x in apellido.upper():
         print(i,"-",x)


if __name__=='__main__':
    run()