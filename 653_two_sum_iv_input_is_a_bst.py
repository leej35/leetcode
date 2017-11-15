# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if root == None: return False
        bst, s = [root], set()
        for i in bst:
            if k-i.val in s: return True
            s.add(i.val)
            if i.left:
                bst.append(i.left)
            if i.right:
                bst.append(i.right)
        return False
