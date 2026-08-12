class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1 longer => False
        if len(s1)> len(s2):
            return False

        s1_count = Counter(s1)
        window = Counter(s2[:len(s1)])
        
        if window == s1_count:
            return True
        
        for i in range(len(s1), len(s2)):
            #add right char
            window[s2[i]] = window.get(s2[i],0)+1
            #remove left char
            left_char = s2[i-len(s1)]
            window[left_char] -=1
            if window[left_char] == 0:
                del window[left_char]
            if window == s1_count:
                return True
        return False