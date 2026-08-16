class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        candidates.sort()

        def dfs(i, cur, total):
            # base
            # if same
            if total == target:
                res.append(cur.copy())
                return
            # if out of bound or too large
            if i >= len(candidates) or total > target:
                return
            # cur new, pop, new
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])
            cur.pop()
            # while same candidates, skip
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            
            dfs(i + 1, cur, total)


        dfs(0, [], 0)
        return res
