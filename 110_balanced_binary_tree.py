# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        not_bal=False
        diffs = []
        
        def visit(node, height):
            if node:
                left, right = visit(node.left,  height), visit(node.right, height)
                diff = abs(left - right)
                diffs.append(diff)
                return height + 1 + max(left,right)
            else:
                return height
        
        visit(root,0)
        
        if len(diffs) > 0 and max(diffs) > 1:
            return False
        return True
