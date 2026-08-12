class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen, res = 0, ""


        for i in range(len(s)):
            # odd
            l, r = i, i
            # while in bound and same
            while 0<=l and r<len(s) and s[l]==s[r]:
                if (r-l+1)>resLen:
                    # increment
                    resLen = r-l+1
                    res = s[l:r+1]
                l-=1
                r+=1
            # even
            l, r = i, i + 1
            # while in bound and same
            while 0<=l and r<len(s) and s[l]==s[r]:
                if (r-l+1)>resLen:
                    # increment
                    resLen = r-l+1
                    res = s[l:r+1]
                l-=1
                r+=1
        return res