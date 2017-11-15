# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # note: BST is a tree which left elements are smaller than center and 
        # right elements are larger than center
        self.s = 0
        def visit(node):
            if node:
                visit(node.right)
                self.s += node.val
                node.val = self.s
                visit(node.left)
        visit(root)
        return root
