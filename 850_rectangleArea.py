from functools import reduce
import itertools


class Solution:
    def rectangleArea(self, rectangles):
        # 这个暴力解会超时
        sum_area = 0
        for size in range(1, len(rectangles) + 1):
            for subset in itertools.combinations(rectangles, size):
                # print("subset", reduce(self.getIntersect, subset), "area:", self.getArea(reduce(self.getIntersect, subset)))
                sum_area += (-1) ** (size + 1) * self.getArea(reduce(self.getIntersect, subset))
        return sum_area % (10 ** 9 + 7)

    def getIntersect(self, rect1, rect2):
        return [max(rect1[0], rect2[0]),
                max(rect1[1], rect2[1]),
                min(rect1[2], rect2[2]),
                min(rect1[3], rect2[3])]

    def getArea(self, rect):
        # 在这里处理没有交集的算出来异常交集点的面积
        dx = max(0, rect[2] - rect[0])
        dy = max(0, rect[3] - rect[1])
        return dx * dy


testObject = Solution()
print(testObject.rectangleArea([[0,0,2,2],[1,0,2,3],[1,0,3,1]]))
