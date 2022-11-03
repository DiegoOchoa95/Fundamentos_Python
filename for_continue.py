#Este codigo devuelve los números pares en el rango de 0 a 1000
def run():
    for contador in range(1000):
        if contador % 2 != 0:
            continue
        print(contador)


if __name__ == '__main__':
    run()
