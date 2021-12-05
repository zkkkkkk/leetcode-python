class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        # 暴力法
        index_a = 0
        index_b = 0
        stack_a = []
        stack_b = []
        while index_a < len(S) or index_b < len(T):
            if index_a < len(S):
                if S[index_a] == "#":
                    try:
                        stack_a.pop()
                    except:
                        pass
                else:
                    stack_a.append(S[index_a])
            if index_b < len(T):
                if T[index_b] == '#':
                    try:
                        stack_b.pop()
                    except:
                        pass
                else:
                    stack_b.append(T[index_b])
            index_a += 1
            index_b += 1

        print("final string a = {}, \n, final string b = {}".format(stack_a, stack_b))
        while stack_a and stack_b:
            if stack_b[-1] != stack_a[-1]:
                break
            stack_a.pop()
            stack_b.pop()
        return not stack_a and not stack_b
    def backspaceCompareWithDoublePointer(self, S, T):
        index_a = len(S) - 1
        index_b = len(T) - 1
        skip_a = 0
        skip_b = 0
        if index_a <0 or index_b < 0:
            return False
        while index_a >= 0 or index_b >= 0:
            while index_a >= 0:
                if S[index_a] == '#':
                    skip_a += 1
                    index_a -= 1
                elif skip_a > 0:
                    skip_a -= 1
                    index_a -= 1
                else:
                    break
            while index_b>= 0:
                if T[index_b] == '#':
                    skip_b += 1
                    index_b -= 1
                elif skip_b > 0:
                    skip_b -= 1
                    index_b -= 1
                else:
                    break
            if index_a >= 0 and index_b >=0:
                if S[index_a] != T[index_b]:
                    return False
            elif index_a >= 0 or index_b >= 0:
                return False
            index_a -= 1
            index_b -= 1
        return True

#123

test_instance =  Solution()
print(test_instance.backspaceCompareWithDoublePointer("ab##","c#d#"))

