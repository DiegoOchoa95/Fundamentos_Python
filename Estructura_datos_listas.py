# Listas de valores en una variable, metodos etc.
def run():
    numero = [1, 2, 3, 4, 5]
    objetos = ["H", 2.3, True, 7000]
    n_desordenado=[1,41,1,78,2,10,8]
    abecedario=["a","z","r","y","b","d","c","ab","re","az"]

    numero[0]=100 #con esto puedo reemplazar un dato de la lista

    numero.append("Diego")  # .append sirve para agregar valores en una lista.
    # .append sirve para agregar valores en una lista.
    objetos.append("Ochoa Orellana")
    # .pop sirve para eliminar valores de esa lista colocando la posicion.
    objetos.pop(1)
    # .insert sirve para insertar un valor en la posicion que queramos.
    numero.insert(2,"Jesucristo")
    # .remove tambien sirve para eliminar un valor de la lista pero indicando el contenido.
    numero.remove(5)
    # .reverse() este metodo sirve para invertir el orden de los valores de una lista.
    numero.reverse()
    # .sort() este metodo sirve para ordenar una lista
    n_desordenado.sort()
    abecedario.sort()
    # fusion de listas
    union=numero+objetos

    print(numero)
    print(objetos)
    print(union)
    print(numero*5)
    print(numero[:2]) #muestra del inicio al valor de la posicion 2 de la lista
    print(4 in numero) #consulta si ese 4 esta en la lista numero
    print(objetos.index(7000)) #muestra la posicion de ese valor en la lista
    print(n_desordenado)
    print(abecedario)
    print(numero.index(3)) #te muestra la posicion de un valor en una lista 


if __name__ == '__main__':
    run()
