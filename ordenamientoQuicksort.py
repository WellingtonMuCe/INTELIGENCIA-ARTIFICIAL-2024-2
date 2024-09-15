def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivote = arr[len(arr) // 2]
    izquierda = [x for x in arr if x < pivote]
    centro = [x for x in arr if x == pivote]
    derecha = [x for x in arr if x > pivote]
    return quicksort(izquierda) + centro + quicksort(derecha)

# Ejemplo de uso
arr = [3, 6, 8, 10, 1, 2, 1]
print(quicksort(arr))  # Output: [1, 1, 2, 3, 6, 8, 10]
