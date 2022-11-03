def run():
    LIMITE=1000000
    contador=0
    potencia_3=3**contador

    while potencia_3<=LIMITE:
        print("3 elevado a la "+ str(contador)+" es: "+str(potencia_3))
        contador=contador+1
        potencia_3=3**contador






if __name__=='__main__':
    run()