class Solution:
    @staticmethod
    def removeOuterParentheses(S):
        '''
        其实就是检查括号匹配，从字符串里把括号匹配的几个子串取出来，然后再去除最外层括号，再拼接
        :return:
        '''
        singleStart = 0
        cur = 0
        parenthesesStack = []
        resultS = ""
        for singleChar in S:
            if singleChar == ')' and len(parenthesesStack) > 1:
                parenthesesStack.pop()
            elif singleChar == ')':
                parenthesesStack.pop()
                resultS += (S[singleStart+1:cur])
                singleStart = cur + 1
            else:
                parenthesesStack.append(singleChar)
            cur += 1
        return resultS


print(Solution.removeOuterParentheses("(()())(())(()(()))"))
