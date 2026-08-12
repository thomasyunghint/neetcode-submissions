class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        
        while l < r:
            if s[l].lower() == " " or s[l].isalnum() == False:
                l+=1
                continue
            if s[r].lower() == " " or s[r].isalnum() == False:
                r-=1
                continue
            if s[l].lower() == s[r].lower():
                l+=1
                r-=1
                continue
            return False
        
        return True