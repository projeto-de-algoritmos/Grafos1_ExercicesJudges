class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        def find_cycle_length(start_node):
            curr = start_node
            path = []
            
            while edges[curr] >= 0:  
                path.append(curr)
                next_node = edges[curr]
                edges[curr] = -1   
                curr = next_node
            
            if curr in path:  
                return len(path) - path.index(curr)  
            else:
                return -1
        
        max_cycle_length = -1
        n = len(edges)
        
        for i in range(n): 
            cycle_length = find_cycle_length(i)
            max_cycle_length = max(max_cycle_length, cycle_length)
        
        return max_cycle_length