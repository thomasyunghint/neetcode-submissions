class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen, res = 0, ""

        for i in range(len(s)):
            # odd
            l, r= i, i
            while 0<=l and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l-=1
                r+=1

            # even
            l, r = i, i+1
            while 0<= l and r<len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l-=1
                r+=1
        return res