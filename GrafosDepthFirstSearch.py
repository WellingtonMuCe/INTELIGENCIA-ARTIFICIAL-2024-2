def dfs(grafo, inicio, visitado=None):
    if visitado is None:
        visitado = set()
    visitado.add(inicio)
    print(inicio, end=" ")

    for vecino in grafo[inicio]:
        if vecino not in visitado:
            dfs(grafo, vecino, visitado)

# Ejemplo de uso
dfs(grafo, 'A')  # Output: A B D E F C
