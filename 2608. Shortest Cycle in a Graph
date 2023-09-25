class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        ans = math.inf

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(curr: int, par: int, dist: int, hmap: Dict[int, List[int]]) -> None:
            nonlocal ans
            if curr in hmap and hmap[curr][1] == 1:
                ans = min(ans, dist - hmap[curr][0])
                return

            vis.add(curr)
            hmap[curr] = [dist, 1]

            for neighbor in graph[curr]:
                if neighbor != par and (neighbor not in hmap or hmap[neighbor][0] > dist + 1 or hmap[neighbor][1] == 1):
                    dfs(neighbor, curr, dist + 1, hmap)

            hmap[curr] = [dist, 0]

        vis = set()

        for i in range(n):
            if i not in vis:
                hmap = defaultdict(list)
                dfs(i, -1, 0, hmap)

        if ans == math.inf:
            return -1
        else:
            return ans
