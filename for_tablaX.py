#Tabla de multiplicar de cualquier número

def run():

    num=int(input("Ingrese el número el cual desea la tabla de multiplicación: "))
    for i in range(0,21):
        print(num,"*",i," es: ", num*i)


if __name__=='__main__':
    run()