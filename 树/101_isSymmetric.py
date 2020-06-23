import queue
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root):
        return self.check(root, root)

    def check(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        return root1.val == root2.val and self.check(root1.left, root2.right) and self.check(root1.right, root2.left)


testNode = TreeNode(0)
testInstance = Solution()
print(testInstance.isSymmetric(testNode))
