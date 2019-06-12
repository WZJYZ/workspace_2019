class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        #1.终止条件
        if not root:
            return True
        '''
        
        left = self.treeDepth(root.left)
        right = self.treeDepth(root.right)
        if abs(left - right) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        '''
        if not self.isBalanced(root.left) or not self.isBalanced(root.right):
            return False
        left = self.treeDepth(root.left)
        right = self.treeDepth(root.right)
        if abs(left - right) > 1:
            return False
        return True

    #返回左右子树的深度
    def treeDepth(self, root):
        if not root:
            return 0
        #if not root.left and not root.right:
        #    return 1
        leftHight = self.treeDepth(root.left)
        rightHight = self.treeDepth(root.right)

        return max(leftHight, rightHight) + 1


s = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(s.isBalanced(root))