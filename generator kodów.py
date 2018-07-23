def generator_kodow(kod1, kod2):
    kod1_lista= kod1.split('-')
    kod2_lista = kod2.split('-')

    kod1_lista = [int(item) for item in kod1_lista]
    kod2_lista = [int(item) for item in kod2_lista]

    while not kod1_lista == kod2_lista:
        if kod1_lista[1] < 999:
            kod1_lista[1] += 1
            if kod1_lista[1] < 10:
                print("{}-00{}".format(kod1_lista[0], kod1_lista[1]))
            elif kod1_lista[1] < 100:
                print("{}-0{}".format(kod1_lista[0], kod1_lista[1]))
            else:
                print("{}-{}".format(kod1_lista[0], kod1_lista[1]))

        else:
            kod1_lista[0] += 1
            kod1_lista[1] = 0
            print("{}-00{}".format(kod1_lista[0], kod1_lista[1]))


generator_kodow('83-300', '84-330')