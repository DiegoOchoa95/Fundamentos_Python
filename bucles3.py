def run():
    LIMITE=5000
    contador=0
    potencia_4=4**contador

    while potencia_4<=LIMITE:
        print("4 elevado a la "+str(contador)+" es: "+ str(potencia_4))
        contador=contador+1
        potencia_4=4**contador



if __name__=='__main__':
    run()