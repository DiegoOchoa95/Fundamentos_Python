#extraer digitos de un numero ingresado
#sumar todos sus digitos
def run():
    numero=int(input("Ingrese un numero: "))
    sumar_digitos=0
    while numero!=0:
        ultimodigito=numero%10
        sumar_digitos=sumar_digitos+ultimodigito
        numero=numero//10
    
    print("SUMA DE DIGITOS: ",sumar_digitos)
        



if __name__=='__main__':
    run()