class TreeNode:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

class Solution1:
    '''
    方法一：利用中序遍历
    输出：bool
    '''
    def isValidBST(self, root):
        inorder = self.inorder(root)
        return inorder == list(sorted(set(inorder)))


    def inorder(self, root):
        if root is None:
            return []
        return self.inorder(root.left) + [root.value] + self.inorder(root.right)

    def inorderTest(self, root):
        if root is None:
            return
        self.inorderTest(root.left)
        print(root.value)
        self.inorderTest(root.right)

class Solution2:

    def isValidBST(self, root):
        self.prev = None
        return self.helper(root)

    def helper(self, root):
        if root is None:
            return True
        if not self.helper(root.left):
            return False
        if self.prev and self.prev.value >= root.value:
            return False
        self.prev = root
        return self.helper(root.right)

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(4)

    s = Solution2()
    print(s.isValidBST(root))
    #s.inorderTest(root)