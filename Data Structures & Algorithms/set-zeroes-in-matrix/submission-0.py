class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rSet = set()
        cSet = set()
        rows, cols = len(matrix), len(matrix[0])
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    rSet.add(r)
                    cSet.add(c)
        for r in range(rows):
            if r in rSet:
                for c in range(cols):
                    matrix[r][c] = 0
        for c in range(cols):
            if c in cSet:
                for r in range(rows):
                    matrix[r][c] = 0