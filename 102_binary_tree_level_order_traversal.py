# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.d={}
        
        def visit(node, l):
            if node:
                visit(node.left, l+1)
                if not self.d.has_key(l): self.d[l]=[]
                self.d[l].append(node.val)
                visit(node.right, l+1)
        
        visit(root,0)
        
        kv = zip(self.d.keys(), self.d.values())
        kv = sorted(kv, key=lambda x:x[0])
        return [x[1] for x in kv]
