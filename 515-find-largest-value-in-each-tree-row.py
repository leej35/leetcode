# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def visit(node, maxvals, depth):
            if node:
                if len(maxvals) <= depth:
                    maxvals.append(node.val)
                if maxvals[depth] < node.val:
                    maxvals[depth] = node.val
                visit(node.left, maxvals, depth+1)
                visit(node.right, maxvals, depth+1)
        
        maxvals = []
        visit(root, maxvals, 0)
        return maxvals
