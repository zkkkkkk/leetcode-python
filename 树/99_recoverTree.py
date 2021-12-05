# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        inorder_array = []
        self.inOrder(root, inorder_array)
        pos_nums = self.find_swap_pos(inorder_array)
        self.act_recover(root, pos_nums, 2)

    def act_recover(self, root, positions, need_change_cnt):
        if positions[0]==-1 or root is None or need_change_cnt == 0:
            return
        print("walk into node val {}".format(root.val))
        if root.val in positions:
            root.val = positions[1] if root.val == positions[0] else positions[0]
            need_change_cnt-=1
        self.act_recover(root.left, positions, need_change_cnt)
        self.act_recover(root.right, positions, need_change_cnt)


    def find_swap_pos(self, path_array):
        x, y = -1, -1
        for i in range(len(path_array)-1):
            if path_array[i] > path_array[i+1]:
                y = path_array[i + 1]
                if x == -1:
                    x = path_array[i]
        return [x, y]



    def inOrder(self, root_node, path_array):
        if root_node is None:
            return
        self.inOrder(root_node.left, path_array);
        path_array.append(root_node.val)
        self.inOrder(root_node.right, path_array)
print(1 in [1,3])