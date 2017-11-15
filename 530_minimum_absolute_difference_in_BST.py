# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    ## NOTE: BST! n.left <= n.val <= n.right
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.s=[]
        def visit(n):
            if n:
                if n.left: visit(n.left)
                self.s.append(n.val)
                if n.right:visit(n.right)
        visit(root)
        # self.s=sorted(self.s) #uncomment if the tree is not BST
        return min([abs(a-b) for a,b in zip(self.s, self.s[1:])])
