class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res= []
        cur = []
        def dfs(start, cur):
            #good when len of combination matches
            if len(cur) == k:
                res.append(cur.copy())
                return
            #recursion
            for _ in range(start, n+1):
                cur.append(_)
                dfs(_+1, cur)
                cur.pop()

        dfs(1, [])
        return res
            

