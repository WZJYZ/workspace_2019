class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #1.错误
    def isSymmetric(self, root: TreeNode) -> bool:
        res = []
        self.inOrder(root, res)
        i = 0
        j = len(res) - 1
        while i <=j:
            if res[i] != res[j]:
                return False
            i += 1
            j -= 1
        return True

    def inOrder(self, root, res):
        #中序遍历
        if not root:
            return

        self.inOrder(root.left, res)
        res.append(root.val)
        self.inOrder(root.right, res)

class Solution2:
    #1.递归
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return t1.val == t2.val and self.isMirror(t1.left, t2.right) and self.isMirror(t1.right, t2.left)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)
#res = []
s = Solution2()
#s.inOrder(root, res)
print(s.isSymmetric(root))