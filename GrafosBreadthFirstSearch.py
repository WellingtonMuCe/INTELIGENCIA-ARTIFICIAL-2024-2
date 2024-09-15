from collections import deque

def bfs(grafo, inicio):
    visitado = set()
    cola = deque([inicio])
    visitado.add(inicio)

    while cola:
        vertice = cola.popleft()
        print(vertice, end=" ")

        for vecino in grafo[vertice]:
            if vecino not in visitado:
                visitado.add(vecino)
                cola.append(vecino)

# Ejemplo de uso
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
bfs(grafo, 'A')  # Output: A B C D E F
