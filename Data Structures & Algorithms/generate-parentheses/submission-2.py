class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = []
        openN, closeN = 0, 0
        def dfs(openN, closeN):
            # base: same
            if openN == closeN == n:
                res.append("".join(cur))
                return
            #add "(" case
            if openN < n:
                cur.append("(")
                dfs(openN+1, closeN)
                cur.pop()
            # add ")" case
            if closeN < openN:
                cur.append(")")
                dfs(openN, closeN+1)
                cur.pop()
        dfs(0,0)
        return res