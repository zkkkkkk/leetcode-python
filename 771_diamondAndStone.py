class Solution:
    def numJewelsInStones(self, J, S):
        '''
        :param J:
        :param S:
        :return:
        '''

        count = 0
        if J is None or S is None or J == " " or S == " ":
            return count
        for singleJewel in J:
            for singleStone in S:
                if singleJewel == singleStone:
                    count+=1
        return count


test = Solution()
print(test.numJewelsInStones('aA', 'aAAbbbb'))
