# Escribe un programa que le solicite al usuario un número entero y
# muestre todos los números correlativos entre el 1 y el número ingresado
# por el usuario.

def run():
    
    numero = int(input("Ingrese un número entero: "))
    i=0
    while i < numero:
        i+=1
        print(i)
    

    #romper flujos de forma forzada
    """
    c=0
    while c<50:
        c+=1
        if c==26:
            break
        print(c)
    """
    #continuar flujo
    """
    c=0
    while c<50:
        c+=1
        if c<26:
            continue
        print(c)
    """  

        
if __name__=='__main__':
    run()