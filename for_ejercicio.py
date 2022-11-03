#Escribe un programa que, dado un número por el usuario,
#muestre todos sus divisores positivos.
#Recordá que un divisor es aquel que divide al número de forma exacta (con resto 0).
def run():
     numero=int(input("Ingrese un numero: "))
     print("Los Dividores exactos de", numero, "son: ")
     
     for i in range(1,numero+1):
        if numero%i==0:
          print(i)



if __name__=='__main__':
   run()
