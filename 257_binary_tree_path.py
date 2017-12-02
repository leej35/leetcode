# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        paths=[]

        def visit(node, path):
            if node:
                path.append(str(node.val))
                if node.left:
                    visit(node.left, copy.deepcopy(path))
                if node.right:
                    visit(node.right, copy.deepcopy(path))
                if not node.left and not node.right:
                    paths.append("->".join(path))
                
        if root: visit(root,[])
        return paths
