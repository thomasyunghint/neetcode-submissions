class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #basecase
        row = [1]*n
        #from lowest rom to top
        for i in range(m-1):
            #make new row for upper row
            newRow = [1]*n
            #fill element from 2nd rightmost: it = its bottom & right
            for j in range(n-2, -1, -1):
                newRow[j] = newRow[j+1] + row[j]
            #replace!
            row = newRow
        #return ans
        return row[0]