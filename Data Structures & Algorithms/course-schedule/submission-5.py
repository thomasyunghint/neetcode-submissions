class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map each course to preList
        preMap = {i:[] for i in range(numCourses)}
        for cre, pre in prerequisites:
            preMap[cre].append(pre)
        visitSet = set()
        #dfs
        def dfs(crs):
            #base
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visitSet.remove(crs)
            preMap[crs] = []
            return True
        # loop check all classes
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True