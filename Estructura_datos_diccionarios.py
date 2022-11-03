def run():
    # primer diccionario
    mi_diccionario = {
        "llave1": 1, "llave2": 2, "llave3": 3
    }

    print(mi_diccionario)

    print(mi_diccionario["llave1"])
    print(mi_diccionario["llave2"])
    print(mi_diccionario["llave3"])

    # segundo diccionario
    dict2 = {
        'nombres': "Diego Eduardo",
        'apellidos': 'Ochoa Orellana',
        "edad": 27,
        "carrera profesional": 'Ingenieria de sistemas e informática'
    }
    print(dict2)
    print(len(dict2))
    print(dict2['edad'])
    print(dict2['nombres'])
    # con el metodo get puedes buscar tambien el valor de una llave del diccionario, y si no lo encuentra te muestra none en vez de un error.
    print(dict2.get('carrera profesional'))
    print(dict2.get('cualquier cosa'))
    # muestra si la llave apodo esta o no en el diccionario
    print("apodo" in dict2)
    print("nombres" in dict2)

    # Tercer diccionario
    persona = {
        'nombre': 'niko',
        'apellido': 'ochoa',
        'lenguajes': ['python', 'java', 'c#'],
        'edad': 7
    }
    print(persona)
    #cambio un valor del diccionario
    persona['nombre']='nicolini'
    print(persona)
    #otras cosas...aumentar la edad
    persona['edad']+=5
    print(persona)
    #como hay una lista en un diccionario puedo agregarle valores
    persona['lenguajes'].append('javascript')
    print(persona)
    #Eliminar un atributo del diccionario
    del persona['apellido']
    print(persona)
    #otra forma de eliminar
    persona.pop('edad')
    print(persona)

    #imprimir los items
    print(persona.items())
    #imprimir las keys
    print(persona.keys())
    #imprimir los valores
    print(persona.values())


if __name__ == '__main__':
    run()
