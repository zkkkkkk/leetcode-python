class Solution:
    def expressiveWords(self, S, words):
        result = []
        for needStretchyWord in words:
            indexS = 0
            indexWord = 0
            while True:
                if S[indexS] == needStretchyWord[indexWord]:
                    indexS += 1
                    indexWord += 1
                elif S[indexWord] == S[indexS]:
                    indexS += 1
                else:
                    if indexS - indexWord + 1 < 3 :
                        break
                    indexWord += 1
                if indexWord == len(needStretchyWord)-1:
                    result.append(needStretchyWord)
                    break
        return result
testObject = Solution()
print(testObject.expressiveWords("heeellooo",["hi", "helo"]))
