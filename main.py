from functools import reduce


def num_impares(x):
    if x % 2 != 0:
        return True
    return False


def suma(a, b):
    return a + b


def main():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    filtrado = list(filter(num_impares, lista))
    reducida = reduce(suma, filtrado)

    print(f'La suma de todos los elementos impares de la lista es {reducida}')


if __name__ == '__main__':
    main()
