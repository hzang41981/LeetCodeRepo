from collections import defaultdict

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        dct = defaultdict(list)
        for pre, crs in prerequisites:
            dct[pre].append(crs)

        print(dct)

        status = [0 for _ in range(numCourses)]

        res = []

        def dfs(n):
            if status[n] == 2:
                return True
            if status[n] == 1:
                return False
            status[n] = 1
            for c in dct[n]:
                dfs(c)
            status[n] = 2
            res.append(n)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return None

        return res

if __name__ == '__main__':
    s = Solution()
    print(s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))