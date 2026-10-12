class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # form adjacency list to traverse graph
        # each node is a class, and each edge leads to a prereq
        prereqs = defaultdict(list)
        for a, b in prerequisites:
            prereqs[a].append(b)

        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if prereqs[crs] == []:
                return True
            
            visited.add(crs)

            for pre in prereqs[crs]:
                if not dfs(pre):
                    return False
            
            visited.remove(crs)
            prereqs[crs] = []
            return True
            

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
            

            
        


        