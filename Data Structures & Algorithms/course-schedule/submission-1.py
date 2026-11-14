class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visitSet = set()   # nodes in current DFS path
        safeSet = set()    # nodes confirmed cycle-free

        def dfs(crs):
            if crs in visitSet:
                return False
            if crs in safeSet:
                return True

            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visitSet.remove(crs)
            safeSet.add(crs)   # memoize: this subtree is safe
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True