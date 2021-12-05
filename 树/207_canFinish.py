import collections
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not prerequisites:
            return True
        graph_matrix = [[0] * numCourses for _ in  range(numCourses)]
        indegree_list = [0] * numCourses
        i = 0
        for edge in prerequisites:
            print(edge)
            for line in graph_matrix:
                print(line)
            print(graph_matrix[edge[1]][edge[0]])
            graph_matrix[edge[1]][edge[0]] =1
            indegree_list[edge[0]] += 1
        # 首轮初始化
        q = collections.deque()
        path = []
        visited = [0] * numCourses
        print("indegree_list", indegree_list)
        for point in range(numCourses):
            if indegree_list[point] == 0:
                path.append(point)
                q.append(point)
                visited[point] = 1
        for line in graph_matrix:
            print(line)
        while q:
            cur_point = q.popleft()
            visited[cur_point] = 1
            for dest in range(numCourses):
                if graph_matrix[cur_point][dest] == 1:
                    indegree_list[dest] -= 1
                if indegree_list[dest] == 0 and visited[dest] != 1:
                    path.append(dest)
                    q.append(dest)
        return  len(path) == numCourses

test_instance = Solution()
print(test_instance.canFinish(3, [[1,0]]))








