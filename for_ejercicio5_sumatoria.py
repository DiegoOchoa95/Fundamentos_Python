#Escribí un programa que, dado un número entero positivo,
#calcule y muestre su sumatoria consecutiva hasta el numero.
def run():
    numero=int(input("Ingrese un numero entero para hallar sumatoria: "))
    z=0
    for i in range(1,numero+1):
        z=z+i
    print("La sumatoria de ",numero, " es: ",z)






if __name__=='__main__':
    run()