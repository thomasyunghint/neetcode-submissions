class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = []
        openN, closeN = 0, 0

        def dfs(openN, closeN):
            #base if same -> add + return
            if openN == closeN == n:
                res.append("".join(cur))
                return
            #try add (
            # not enough openN
            if openN < n:
                cur.append("(")
                dfs(openN+1, closeN)
                cur.pop()
            #try add )
            # not enough closeN
            if closeN < openN:
                cur.append(")")
                dfs(openN, closeN+1)
                cur.pop()
        dfs(0, 0)
        return res