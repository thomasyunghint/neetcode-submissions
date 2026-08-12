class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #res defaultdict
        res = defaultdict(list)
        #loop strs
            #open count [0]
            #loop c in s
                #count[? - ? ] ?= 1
            #res[tuple(?)].?(?)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord("a")] +=1
            res[tuple(count)].append(s)

        #return ?
        return list(res.values())