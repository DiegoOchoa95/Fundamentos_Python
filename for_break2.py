def run():
    frase = input("Ingrese una frase: ")
    for i in frase:
        if i == "o":
            break
        print(i)


if __name__ == '__main__':
    run()
