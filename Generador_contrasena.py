# Pequeño proyecto que genera contraseñas aleatoreamente
import random


def generar_contrasena():
    mayusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                  "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    minusculas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                  "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    simbolos = ["!", "#", "$", "&", "/", "(", ")", "?", "¡", "¿", "%"]
    numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    caracteres = mayusculas+minusculas+simbolos+numeros
    contrasena=[]

    for i in range(15): #este for almacenara 15 valores para una contraseña aleatoria
        caracter_random=random.choice(caracteres) #random.choice te genera un valor aleatorio de una lista
        contrasena.append(caracter_random) #agrego el valor lo obtenido en la lista contrasena[]
    
    contrasena="".join(contrasena) #Esta linea de codigo lo que hace es convertir en string toda la lista
    return contrasena #regreso un valor, ya que si no lo agrego valadria None



def run():
    contrasena = generar_contrasena()
    print("Tu nueva contraseña es: " + contrasena)


if __name__ == '__main__':
    run()
