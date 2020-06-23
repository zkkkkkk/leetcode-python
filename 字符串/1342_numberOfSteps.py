class Solution:
    def numberOfSteps (self, num: int) -> int:
        '''
        暴力解就行了，位运算的感觉没必要
        :param num:
        :return:
        '''
        processCnt = 0
        if num == 0:
            return 0
        while num != 0:
            processCnt += 1
            if num % 2 == 0:
                num /= 2
            else :
                num -= 1
        return processCnt

testObject = Solution()
print(testObject.numberOfSteps(0))