def czy_w_liscie(lista, n):
    nowa_lista = [x for x in range(1, n+1) if x not in lista]
    return nowa_lista


print(czy_w_liscie([2, 3, 7, 4, 9], 10))
