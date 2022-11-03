# Ingresar un numero y mostrar cuantos digitos son pares e impares.

def run():     
        numero = int(input("Ingrese un numero: "))
        d_par = 0
        d_impar = 0
        while numero != 0:        
            ultimodigito = numero % 10           
            if ultimodigito % 2 == 0:
                d_par += 1
            else:
                d_impar += 1
            numero = numero//10
               
        print("digito par",d_par)
        print("digito impar",d_impar)
        
        


if __name__ == '__main__':
    run()
