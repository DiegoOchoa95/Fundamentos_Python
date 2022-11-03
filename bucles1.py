#MI CODIGO PERO OTRO ANALISIS
# imprimir todas las potencias de 2 hasta llegar a la potencia 1000
# 2 formas de hacerlo con un for y un while


# while
def run():  # definimos una funcion y dentro de ella escribimos el codigo, el nombre de la funcion puede ser cualquiera que te guste
    contador = 0
    while contador <= 10:
        print(" 2 elevado a la "+str(contador) + " es: " + str(2**contador))
        contador += 1


if __name__ == '__main__':  # colocamos la siguiente linea de codigo para indicar de donde iniciará el programa en python, parte de las buenas practicas
    run()


# for

#contador = 0
# for contador in range(20):
    #print(" 2 elevado a la "+str(contador)+ " es: " + str(2**contador))
    #contador += 1
