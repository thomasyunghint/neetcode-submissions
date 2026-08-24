class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        a, b = len(word1), len(word2)

        for i in range(max(a, b)):
            if i < a:
                res += word1[i]
            if i < b:
                res += word2[i]
        return res