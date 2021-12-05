import treeBase
class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        p = []
        def innerWalk(node, path):
            if not node:
                return None
            if node == target:
                return path
            innerWalk(target.left, path+[0])
            innerWalk(target.right, path+[1])
        walk_path = innerWalk(original, [])
        if not walk_path:
            return None
        for direct in walk_path:
            if direct == 0:
                cloned = cloned.left
            else:
                cloned = cloned.right
        return cloned





