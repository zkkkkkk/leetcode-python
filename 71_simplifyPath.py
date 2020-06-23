class Solution:
    @staticmethod
    def simplifyPath(self, path: str) -> str:
        needProcessList = path.split("/")
        tempStack = []
        for singlePath in needProcessList:
            if singlePath in ['', '.']:
                continue
            elif singlePath == '..':
                if len(tempStack) > 0 :
                    tempStack.pop()
            else:
                tempStack.append(singlePath)
        return "/"+str.join("/",tempStack)





