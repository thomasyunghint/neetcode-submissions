class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #if s1 longer, False


        s1_count = Counter(s1)
        window = Counter(s2[:len(s1)])

        if window == s1_count:
            return True
    
        for r in range(len(s1), len(s2)):
            # add right char
            window[s2[r]] = window.get(s2[r],0)+1
            # remove left char
            left_char = s2[r-len(s1)]
            window[left_char] -= 1 
            # if == 0, remove
            if window[left_char] == 0:
                del window[left_char]
            # return true
            if window == s1_count:
                return True
        return False