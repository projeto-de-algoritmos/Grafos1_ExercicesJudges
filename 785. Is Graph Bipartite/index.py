from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [-1] * n  # Lista de cores dos vértices. -1 significa que o vértice ainda não foi colorido.

        def dfs(u: int, color: int) -> bool:
            colors[u] = color
            for v in graph[u]:
                if colors[v] == color:  # Se um vizinho tem a mesma cor que o vértice atual, o grafo não é bipartido
                    return False
                if colors[v] == -1 and not dfs(v, 1 - color):  # Se o vizinho ainda não foi colorido, chame a DFS recursivamente com a cor oposta
                    return False
            return True
        
        for u in range(n):
            if colors[u] == -1 and not dfs(u, 0):  # Se o vértice não foi colorido, chame a DFS com cor 0
                return False
        return True