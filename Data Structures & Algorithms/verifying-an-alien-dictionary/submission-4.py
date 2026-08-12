class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        # c,i map
        orderInd = {c:i for i,c in enumerate(order)}


        #loop words
        for i in range(len(words)-1):
            #get w1, w2
            w1,w2 = words[i], words[i+1]
            for j in range(len(w1)):
                # if w2 end first, False
                if j == len(w2):
                    return False

                # if not same:
                if w1[j] != w2[j]:
                     # if w2 index < w1 index: False
                    if orderInd[w2[j]] < orderInd[w1[j]]:
                        return False
                    break
        #True
        return True
