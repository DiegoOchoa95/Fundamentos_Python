def run():

    palabra=input("Ingresa una palabra: ")
    palabra=palabra[0] 
    print(palabra)
    
    palabra2=input("Ingresa una palabra2: ")
    palabra2=palabra2[0:3] 
    print(palabra2)

    palabra3=input("Ingresa una palabra3: ")
    palabra3=palabra3[0: :2] 
    print(palabra3)

if __name__=='__main__':
    run()