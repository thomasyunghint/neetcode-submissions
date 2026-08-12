class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        s = s.lower()
        while l < r:
            if s[l] == " " or s[l].isalnum() == False:
                l+=1
                continue
            if s[r] == " " or s[r].isalnum() == False:
                r-=1
                continue
            if s[l] == s[r]:
                l+=1
                r-=1
                continue
            return False
        
        return True