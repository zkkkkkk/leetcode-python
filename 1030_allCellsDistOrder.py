from collections import defaultdict
class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        max_dist = R + C - 2
        dist_cell_list = [[] for i in range(max_dist+1)]
        for row in range(R):
            for col in range(C):
                dist_cell_list[abs(row - r0) + abs(col - c0)].append([row, col])
        result_list = []
        for this_dist_list in dist_cell_list:
            result_list.extend(this_dist_list)
        return result_list

    def allCellsDistOrderBfs(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """

        dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        maxDist = max(r0, R - 1 - r0) + max(c0, C - 1 - c0)
        row, col = r0, c0
        ret = [[row, col]]
        for dist in range(1, maxDist + 1):
            row -= 1
            print("每个距离的起始点:({}, {})".format(row, col))
            for i, (dr, dc) in enumerate(dirs):
                print(i)
                while (i % 2 == 0 and row != r0) or (i % 2 != 0 and col != c0):
                    print(dr, dc)
                    # print("全量坐标,横坐标:{}, 纵坐标{}".format(row, col))
                    if 0 <= row < R and 0 <= col < C:
                        ret.append([row, col])
                        # print("保留的数据，横坐标:{}, 纵坐标{}".format(row, col))
                    row += dr
                    col += dc
        return ret
print(Solution().allCellsDistOrderBfs(2,30,1,2))
