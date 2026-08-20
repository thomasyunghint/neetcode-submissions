class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""

        for i in range(len(strs[0])):
            for word in strs:
                #if out of bound or not same char -> return res
                if i == len(word) or word[i] != strs[0][i]:
                    return res
            #it's good now(same char & in bound):concat
            res += strs[0][i]
        return res
