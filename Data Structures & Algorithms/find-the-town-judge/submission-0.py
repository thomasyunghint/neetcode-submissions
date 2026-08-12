class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        

        if n == 1:
            return 1
        #Trust
        Score = [0]*(n+1)
        #add a,b in Trust (a trust b)
        for [a,b] in trust:
            Score[b] += 1
            Score[a] -= 1

        for i in range(1, n+1):
            if Score[i] == n-1:
                return i

        return -1