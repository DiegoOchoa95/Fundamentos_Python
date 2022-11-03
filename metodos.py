#ingreso una palabra y lo convierto a mayuscula con el metodo .upper()
#nombre.upper() = coloca todo en mayusculas.
#nombre.capitalize() = coloca la primera letra en mayusculas.
#nombre.strip() = elimina todos los espacios en blanco de un texto al inicio y al final.
#nombre.lower() = coloca toda la palabra o frase en minusculas.
#nombre.replace('o','a') = reemplaza valores en un texto.
#nombre.count('a')= este metodo cuenta cuantas letras a hay en un texto.
#nombre.swapcase()=este metodo convierte los mayusculas en minusculas y viceversa.
#nombre.startswitch('goku')= este metodo muestra si el texto empieza con goku, y arroja True.
#nombre.endswith('kakaroto')=este metodo muestra si el texto termina en kakaroto, y arroja True si es cierto.
#nombre.title()=este metodo arroja todas las iniciales en mayuscula.
#nombre[0] = te muestra el caracter segun la posicion indicada.
#nombre[1] = te muestra el caracter segun la posicion indicada.
#nombre[0:2] = te muestra desde la posicion 0 hasta la posicion 2.
#nombre[0:2:4] = te muestra desde la posicion 0 hasta la posicion 2 de 4 en 4.
#nombre[10:16:2]=te muestra de la posicion 10 a la 16, saltando 2 caracteres.
#nombre[::2]=salta 2 caracteres de todo el texto.
#nombre[::-1] = te muestra el nombre al revez.
#nombre[:10]=te muestra del inicio hasta la posicion 10.
#nombre[5:]=te muestra de la posicion 5 hasta la final.
#nombre[:]=te muestra todo jaa.
#nombre[-1]=te muestra la letra de la ultima posicion de un texto.
#nombre[-2]=te muestra la letra de la penultima posicion de un texto.
#nombre[-3]=te muestra la letra de la antepenultima posicion de un texto. etc etc
#len(nombre) = te cuenta la cantidad de caracteres de una palabra o una frase.
# https://www.w3schools.com/python/python_strings_methods.asp
# etc
def run(): #buena practica
    titulo=input("Ingrese un titulo para una empresa de tecnologias: ")
    titulo=titulo.upper()

    print(titulo)

if __name__=='__main__':
    run()  #buena practica