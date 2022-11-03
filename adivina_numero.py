#MI CODIGO-ADIVINA EL NUMERO
import random

def run():
    numero = int(input("Ingresa un número del 1 al 100: "))
    n_aleatorio = random.randint(0, 100)
    while numero <= 100:
        if numero != n_aleatorio:
            if numero < n_aleatorio:
                print("Sigue intentando,INGRESA UN NUMERO MAS ALTO")
            else:
                print("Sigue intentando,INGRESA UN NÚMERO MAS BAJO")
            numero = int(input("Ingresa un número del 1 al 100: "))

        else:
            print("GANASTES!!! FELICITACIONES!!!")
            break


if __name__ == '__main__':
    run()
