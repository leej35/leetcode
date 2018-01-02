class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums:
            pos = nums.index(max(nums))
            
            node = TreeNode(nums[pos])
            node.left = self.constructMaximumBinaryTree(nums[:pos])
            node.right = self.constructMaximumBinaryTree(nums[pos+1:])
            return node
