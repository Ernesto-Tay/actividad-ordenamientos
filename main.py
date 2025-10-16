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

while True:
    print("\n\n----------SISTEMA DE ORDENAMIENTO DE LISTA----------\n1. Crear una lista\n2. Ver lista actual\n3. Ordenar con bubble sort\n4. Ordenar con quick sort\n5. Ordenar con selection sort\n6. Ordenar con bogo sort\n7. Salir")
    select = input("Seleccione una opción: ")
    match select:
        case "1":
            pass
        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case "5":
            pass
        case "6":
            pass
        case "7":
            print("Saliendo...")
            break
        case _:
            print("Opción inválida")