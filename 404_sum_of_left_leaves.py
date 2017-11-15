# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.s = 0
        def visit(n):
            if n:
                if n.left:
                    visit(n.left)
                    if n.left.left == None and n.left.right == None:
                        self.s+=n.left.val
                if n.right:
                    visit(n.right)
                    
        visit(root)
        return self.s
    
