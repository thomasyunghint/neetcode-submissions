class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        cur = []
        digitToChar = { 
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"}
        def dfs(i, cur):
            # if same length -> append copy
            if i == len(digits):
                res.append("".join(cur))
                return
            # explore
            for c in digitToChar[digits[i]]:
                cur.append(c)
                dfs(i+1, cur)
                cur.pop()
        if digits:
            dfs(0, [])
        return res