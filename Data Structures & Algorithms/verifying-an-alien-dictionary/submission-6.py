class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        #hashMap for comparison
        orderInd = {c:i for i,c in enumerate(order)}

        #loop words
        for i in range(len(words)-1):
            #w1 , w2
            w1, w2 = words[i], words[i+1]
            #check each j in len(w1)
            for j in range(len(w1)):
                #if w1 longer -> False 
                if j == len(w2):
                    return False
                #if not same
                if w2[j] != w1[j]:
                    # w2 index < w1 index -> False
                    if orderInd[w2[j]] < orderInd[w1[j]]:
                        return False
                    break
        return True