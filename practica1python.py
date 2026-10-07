def main():

    lista1 = ["Mario", "Wario", "Luigi"]

    lista2 = ["Toad", "Toadette", "Huesitos"]

    lista1.extend(lista2)

    print("Último elemento de la lista:", lista1[-1])

    numeros = (2, 4, 6)

    print("Primer elemento de la tupla:", numeros[0])

    inicio = int(input("Introduce el inicio del rango: "))
    fin = int(input("Introduce el fin del rango: "))
    salto = int(input("Introduce el salto del rango: "))

    rango = range(inicio, fin, salto)

    print("Rango creado:", list(rango))


if __name__ == "__main__":
    main()