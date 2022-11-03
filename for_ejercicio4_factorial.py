#Escribí un programa que, dado un número entero positivo,
#calcule y muestre su factorial.
#El factorial de un número se obtiene multiplicando
#todos los números enteros positivos que hay entre el 1 y ese número.
#El factorial de 0 es 1.
def run():
    numero=int(input("Ingrese un numero para hallar su factorial: "))
    f=1
    for i in range(1,numero+1):
        f=f*i
    print("El factorial de ", numero, " es: ", f)



if __name__=='__main__':
    run()
