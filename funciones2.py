#al definir esta funcion, creo un parámetro llamado mensaje, ya que es lo unico que cambiará luego
def conversacion(mensaje):
    print("Hola soy Diego")
    print("Como estas")
    print(mensaje)
    print("Adios, Dios te bendiga")

opcion=int(input("Ingresa una de estas opciones (1, 2, 3, 4): "))

if opcion==1:
        conversacion("ELEGISTES LA OPCION NÚMERO 1")
elif opcion==2:
        conversacion("ELEGISTES LA OPCION NÚMERO 2")
elif opcion==3:
        conversacion("ELEGISTES LA OPCION NÚMERO 3")
elif opcion ==4:
        conversacion("ELEGISTES LA OPCION NÚMERO 4")
else:
        print("por favor ingresar la opcion correcta, gracias")
