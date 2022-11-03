# Escribí un programa que, dada una frase por el usuario,
# muestre la cantidad total de vocales (tanto mayúsculas como minúsculas)
# que contiene.

def run():
    frase = input("Ingrese una frase: ")
    vocales = "aeiouAEIOU"
    cantidad = 0
    for i in frase:
        if i in vocales:
            cantidad = cantidad+1
    print("Vocales:", cantidad)


if __name__ == '__main__':
    run()
