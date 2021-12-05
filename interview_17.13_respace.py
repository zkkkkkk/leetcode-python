import bintrees

class Solution(object):
    def respace(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: int
        """
        dp_result = [0]*(len(sentence)+1)
        word_dict = {}
        for key in dictionary:
            word_dict[key] = 0
        trieTree = Trie()

        dp_result[0] = 0
        for index in range(0, len(sentence)):
            dp_result[index+1] = dp_result[index] + 1
            for inner_index in range(0, index+1):
                if word_dict.__contains__(sentence[inner_index:index+1]):
                    dp_result[index+1] = min(dp_result[inner_index], dp_result[index+1])


        # for index in range(1, len(sentence)+1):
        #     for inner_index in range(1, index):
        #         if word_dict.__contains__(sentence[inner_index-1:index-1]):
        #             dp_result[index] = min(dp_result[inner_index-2], dp_result[index-2] + 1)
        #         else:
        #             dp_result[index] = dp_result[index-2] + 1
        #             # print(" simple add")
        return dp_result[-1]
test_solution = Solution()
print(test_solution.respace(dictionary = ["looked","just","like","her","brother"],sentence = "jesslookedjustliketimherbrother"))

