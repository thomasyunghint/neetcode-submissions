class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2): return False
        l=0
        s1_count = [0]*26
        window_count= [0]*26
        for c in s1:
            s1_count[ord(c)-ord('a')]+=1
        for k in range(len(s1)):
            window_count[ord(s2[k])-ord('a')] +=1 
        if s1_count == window_count:
            return True
        for r in range(len(s1), len(s2)):
            window_count[ord(s2[r])-ord('a')]+=1
            window_count[ord(s2[l])-ord('a')]-=1
            l+=1
            if s1_count ==window_count:
                    return True  

        return False
