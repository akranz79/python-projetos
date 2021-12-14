import random
from sorting import insertion_sort, selection_sort, bubble_sort, mergesort

any_numbers = random.sample(range(1, 1000), 15)

already_sorted = [1, 2, 3, 16, 20, 34, 45, 54, 57, 80, 91, 99, 102, 199, 250]

inversed = [250, 199, 102, 99, 91, 80, 57, 54, 45, 34, 20, 16, 3, 2, 1]

repeated = [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 7, 7, 3, 2, 1]

if __name__ == "__main__":
    lista = any_numbers
    print(lista)
    mergesort(lista)
    print("\n Ordenado: ")
    print(lista)