class Tree:
    rootNode = None

    def __init__(self, x = None):
        self.rootNode = x

    def gen_from_array(self, node_array):
        if len(node_array) == 0:
            print("error gen from null array")
            return None
        self.rootNode = TreeNode(node_array[0])
        treenode_array = [self.rootNode]
        for i in range(1, len(node_array)):
            if treenode_array[i-1] is not None:
                treenode_array[i-1].left = TreeNode(node_array[2*i]) if 2*i < len(node_array) and node_array[2*i] is not None else None
                treenode_array[i-1].right= TreeNode(node_array[2*i+1]) if 2*i+1 < len(node_array) and node_array[2*i+1] is not None else None
                treenode_array[2*i] = treenode_array[i-1].left
                treenode_array[2*i + 1] = treenode_array[i-1].right




class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
