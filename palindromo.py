#los palindromos son palabras que se leen igual al revez y al derecho
#ejemplos: ana, luz azul, etc

#definimos una funcion para eliminar los espacios de unas palabras o frases palidromas.
def palindromo(palabra):
    palabra=palabra.replace(' ','') #reemplazamos el espacio por la nada 
    palabra=palabra.lower() #convertimos la palabra en minuscula para que la computadora lo pueda ver igual al revez y al derecho
    palabra_invertida=palabra[::-1] #convertimos la palabra al revez 
    if palabra==palabra_invertida:
        return True   #va a devolver el valor de True
    else:
        return False  #va a devolver el valor de False

def run():
    palabra=input("Ingresa una palabra: ")
    es_palindromo=palindromo(palabra)
    if es_palindromo== True:
        print("La palabra ingresada ES PALINDROMO")
    else:
        print("La palabra ingresada NO ES PALINDROMO")   



if __name__=='__main__':
    run()
    #el entrypoint o el punto de entrada, osea en un programa de python se ejecuta todo desde aqui es para una buena practica.
    # run().........