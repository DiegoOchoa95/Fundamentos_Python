def run():
    pais_poblacion={
        "PERU":30,
        "BRASIL":100,
        "ARGENTINA":50,
        "BOLIVIA": 20,
        "COLOMBIA":35,
        "CHILE":20,
        "PARAGUAY":25,
        "URUGUAY":15,
        "ECUADOR":18
    }
    for i in pais_poblacion.keys():
        print("Llaves de mi diccionario: ")
        print(i)
    
    for j in pais_poblacion.values():
        print("Los valores de mi diccionario son: ")
        print(j)

    for i,j in pais_poblacion.items():
        print("En el pais de "+i+" hay "+str(j)+" millones de habitantes")
        




if __name__=='__main__':
    run()