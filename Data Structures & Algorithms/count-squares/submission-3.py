class CountSquares:

    def __init__(self):
        self.ptsCount = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        dx, dy = point
        for x, y in self.pts:
            if (abs(dx-x) != abs(dy-y) or x==dx or y==dy):
                continue
            res += self.ptsCount[(x,dy)] * self.ptsCount[(dx,y)]
        return res
