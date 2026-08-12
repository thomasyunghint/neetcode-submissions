class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1 longer => False

        s1_count = Counter(s1)
        window = Counter(s2[:len(s1)])

        if window == s1_count:
            return True
        
        for i in range(len(s1), len(s2)):
            #add right char
            window[s2[i]]=window.get(s2[i],0)+1
            #remove left char
            window[s2[i-len(s1)]] -=1
            if window[s2[i-len(s1)]] == 0:
                del window[s2[i-len(s1)]]
            if window == s1_count:
                return True
        return False