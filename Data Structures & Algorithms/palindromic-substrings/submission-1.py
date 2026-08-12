class Solution:
    def countSubstrings(self, s: str) -> int:
        paliCount = 0

        for i in range(len(s)):
            # paliCount+=1
            #odd
            l, r = i, i
            #while in bound, and s[l]==s[r]
            while 0<=l and r<len(s) and s[l] == s[r]:
                paliCount+=1
                l-=1
                r+=1
            #even
            l, r = i, i + 1
            #while in bound, and s[l]==s[r]
            while 0<=l and r<len(s) and s[l] == s[r]:
                paliCount+=1
                l-=1
                r+=1
        return paliCount