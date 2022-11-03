#mi codigo

def run():
    """
    for num in range(1001):
        print(num)
    """
    #otra forma
    """
    for i in range(1,1001): #inicializamos desde el 1 al 1000
        print(i)
    """
    
    #listas en for
    lista=[15,42,78,32,16,96,120,81]
    for i in lista:
        print(i)

    #tuplas en for
    tupla=("diego","jose","andres","felix","eugenia","virginia")
    for i in tupla:
        print(i)

    #diccionario en for
    producto={
        "nombre":"camisa",
        "precio":60,
        "stock":10,
        "marca":"polistel"
    }
    for i in producto:
        print(i) #muestra solo las llaves
        print(i,"=",producto[i]) #con esto muestra completo
    
    for i,f in producto.items(): # con este for podremos mostrar todos  los items del diccionario
        print(i,"=",f)

    #lista de diccionarios
    persona=[ {
        'nombre':'nico',
        'edad':34
    },
    {
        'nombre':'emma',
        'edad':45
    },
    {
        'nombre':'david',
        'edad':52

    },
    {
        'nombre':'luis',
        'edad':38
    }]
    for i in persona:
        print(i)
    for i in persona:
        print("nombre: ",i['nombre'])
    for i in persona:
        print("edad: ",i['edad'])
    
    #CICLOS ANIDADOS
    matriz=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]] #una lista de listas
    print(matriz[0]) #imprime el primer valor de la lista grande
    print(matriz[0][1])#imprime el primer valor de la lista grande, pero de la posicion 1 de esa lista.
    
    for i in matriz: #ciclo anidado que muestra la lista y luego sus respectivos valores.
        print(i)       
        for f in i:  #NOTA: las letras i y f, pueden varias y cambiar a gusto del programador,
            print(f) #por ejemplo en este for anidado, el i vendria a  ser la fila y f la columna de la matriz.




if __name__=='__main__':
    run()