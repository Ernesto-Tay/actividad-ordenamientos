import random
import time
main_list = []

def bubble_sort(lista):
    for i in range(len(lista)-1):
        for j in range(len(lista)-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

def refresh_list(lista, length):
    lista.clear()
    for i in range(length):
        lista.append(random.randint(1, 999))
    return lista

refresh_list(main_list, 5)
def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista[round(len(lista) / 2, 0)]
    lower = [val for val in lista if val < pivot]
    higher = [ val for val in lista if val > pivot ]
    middle = [ val for val in lista if val == pivot ]
    return quick_sort(lower) + middle + quick_sort(higher)

def selection_sort(lista):
    for i in range(len(lista)):
tiempo = bubble_sort(lista)
print(tiempo)

fin = time.perf_counter()

print(f"Tiempo de ejecución: {fin - inicio:.5f} segundos")

def selection_sort(list):
    for i in range(len(list)):
        min_index = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]

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
        list[i], list[min_index] = list[min_index], list[i]

