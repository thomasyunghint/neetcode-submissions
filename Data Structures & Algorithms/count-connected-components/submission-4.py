class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        #build adjacent hashmap
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visit = [False] *n

        #dfs: turns all to true in visit
        def dfs(node):
            for nei in adj[node]:
                if visit[nei] == False:
                    visit[nei] = True
                    dfs(nei)

        res=0
        #for loop: if not visit-> turn to Yes, and turns adjacent
        for node in range(n):
            if visit[node] == False:
                visit[node] = True
                dfs(node)
                res+=1

        return res