def generator_kodow(kod1, kod2):     # TODO: drukuje ostatni drugi z podanych kodów, a nie powinien
    kod1lista = kod1.split('-')
    kod2lista = kod2.split('-')
    kod1lista[0] = int(kod1lista[0])
    kod1lista[1] = int(kod1lista[1])
    kod2lista[0] = int(kod2lista[0])
    kod2lista[1] = int(kod2lista[1])

    while not kod1lista == kod2lista:
        if kod1lista[1] < 999:
            kod1lista[1] += 1
            if kod1lista[1] < 10:
                print("{}-00{}".format(kod1lista[0], kod1lista[1]))
            elif kod1lista[1] < 100:
                print("{}-0{}".format(kod1lista[0], kod1lista[1]))
            else:
                print("{}-{}".format(kod1lista[0], kod1lista[1]))

        else:
            kod1lista[0] += 1
            kod1lista[1] = 0
            print("{}-00{}".format(kod1lista[0], kod1lista[1]))


print(generator_kodow('83-300', '85-330'))
