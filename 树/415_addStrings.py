import math
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1 = len(num1)
        l2 = len(num2)
        p1 = l1 - 1
        p2 = l2 - 1
        add = 0
        result = ""
        while p1 >= 0 or p2 >= 0 or add != 0:
            this_num1 = 0 if p1 < 0 else int(num1[p1])
            this_num2 = 0 if p2 < 0 else int(num2[p2])
            # print("num 1 = {}, num 2 = {}".format(this_num1, this_num2))
            # temp_res = (this_num1 + this_num2) % 10 + add
            result += str((this_num1 + this_num2 + add) % 10)
            add = math.floor((this_num1 + this_num2 + add) / 10)
            # print("add = {}, res = {}".format(add, temp_res))

            p1 -= 1
            p2 -= 1
        return result[::-1]
test_instance = Solution()
print(test_instance.addStrings("1","9"))
