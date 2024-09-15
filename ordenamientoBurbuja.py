def ordenamiento_burbuja(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
print(ordenamiento_burbuja(arr))  # Output: [11, 12, 22, 25, 34, 64, 90]
