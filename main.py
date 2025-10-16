import random
import time
main_list = None

def refresh_list(length):
    new_list = []
    for i in range(length):
        new_list.append(random.randint(1, 999))
    return new_list

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista[round(len(lista) / 2, 0)]
    lower = [val for val in lista if val < pivot]
    higher = [ val for val in lista if val > pivot ]
    middle = [ val for val in lista if val == pivot ]
    return quick_sort(lower) + middle + quick_sort(higher)


def is_sorted(lista):
    return all(lista[i] <= lista[i+1] for i in range(len(lista)-1))
def bogo_sort(lista):
    tries = 0
    while not is_sorted(lista):
        tries += 1
        random.shuffle(lista)
        tries += 1
    return lista, tries
