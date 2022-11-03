def run():
    edad_personas = {
        "pedro": 15,
        "miguel": 20,
        "diego": 27,
        "jose": 25,
        "andres": 31,
        "jorge": 42
    }
# en el presente for el metodo .keys() me arroja las llaves de mi diccionario
    for i in edad_personas.keys():  
        print(i)

# en el presente for el metodo .values() me arroja los valores de mi diccionario
    for j in edad_personas.values():
        print(j)

# en el presente for el metodo .items() me arroja
# todo el diccionario completo, tanto llaves como valores
    for k in edad_personas.items():
        print(k)


if __name__ == '__main__':
    run()
