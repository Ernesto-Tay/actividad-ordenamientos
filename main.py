import time
lista = [1,2,5,62,272,234,1,0,124,44,3,2,789,84,7,89]
inicio = time.perf_counter()

def bubble_sort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

tiempo = bubble_sort(lista)
print(tiempo)

fin = time.perf_counter()

print(f"Tiempo de ejecución: {fin - inicio:.5f} segundos")

def selection_sort(list):
    for i in range(len(list)):
        min_index = i
        for j in range(i+1, len(list)):
            if list[j] < list[min_index]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]

