from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Inicializa o vetor de pais para cada nó
        parents = [i for i in range(len(edges) + 1)]

        # Função para encontrar o pai de um nó usando Union-Find
        def find(x):
            if parents[x] == x:
                return x
            else:
                parents[x] = find(parents[x])
                return parents[x]

        # Função para unir dois conjuntos usando Union-Find
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parents[px] = py

        # Percorre as arestas e verifica se a adição de cada uma delas forma um ciclo
        for edge in edges:
            if find(edge[0]) == find(edge[1]):
                return edge
            else:
                union(edge[0], edge[1])

        # Se não houver ciclo, retorna a última aresta
        return edges[-1]