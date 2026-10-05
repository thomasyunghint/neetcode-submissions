class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])
        res = []
        x, y, dx, dy = 0, 0, 1, 0

        for _ in range(ROWS * COLS):
            res.append(matrix[y][x])
            matrix[y][x] = "#"
            if not 0 <= x + dx < COLS or not 0 <= y + dy < ROWS or matrix[y + dy][x + dx] == "#":
                dx, dy = -dy, dx
            x += dx
            y += dy
        return res
