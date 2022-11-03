# la Tuplas a diferencia de las listas, son estaticas, y mas rapidas de aplicar 
# En este caso no se pueden agregar valores (.append) ni eliminar valores (.pop)
import random


def run():
    mi_tupla=(1,2,3,4,5,5,5,5)

    for i in mi_tupla:
        print(i)

    print(mi_tupla)
    print(type(mi_tupla)) #muestra el tipo de dato
    print(mi_tupla.index(3)) #muestra la posicion del numero 3
    print(mi_tupla.count(5)) #cuenta los valores igual a 5

    #convertir una tupla a list
    mi_lista=list(mi_tupla)
    print(mi_lista)
    print(type(mi_lista))

    #viceversa
    mi_tupla=tuple(mi_lista)
    print(mi_tupla)
    print(type(mi_tupla))

    #Escojer una opcion aleatorio de una tupla
    tupla2=("diego","jose",21,45,"Andres",2022)
    aleatorio=random.choice(tupla2)
    print(aleatorio)




if __name__=='__main__':
    run()