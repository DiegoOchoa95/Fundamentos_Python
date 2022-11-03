#Este codigo devuelve los números impares en el rango de 0 a 1000
def run():
    for i in range(1000):
        if i % 2 == 0:
            continue
        print(i)


if __name__ == '__main__':
    run()
