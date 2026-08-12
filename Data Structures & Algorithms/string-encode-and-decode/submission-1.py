class Solution:

    def encode(self, strs: List[str]) -> str:
        #res string
        res = ""
        #for each strs, append its length & a "#" & strs itself to res
        for s in strs:
            res += str(len(s))+"#"+ s
        #return res
        return res
    def decode(self, s: str) -> List[str]:
        #res list, point i
        res = []
        i = 0
        # while i in bound
        while i < len(s):
            # j=i
            j=i
            # while str[j] =/= "#":
                #j+1
            while s[j] != "#":
                j+=1
            #length = length of str[i:j]
            length = int(s[i:j])
            #res 加 str ? : ?
            res.append(s[j+1:j+1+length])
            #i= beginning of next string
            i=j+1+length
        #return res
        return res