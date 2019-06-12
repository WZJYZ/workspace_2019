class TreeNode:

    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None

class Solution1:
    def maxDepth(self, root: TreeNode) -> int:

        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

class Solution2:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        import collections
        queue = collections.deque()
        queue.append(root)
        level = 0
        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return level
class Solution3:
    #理解递归
    def maxDepth(self, root: TreeNode) -> int:
        # 1.找终止条件，当树为空时结束递归，并返回当前深度为0
        if not root:
            return 0
        # 2.找返回值，返回左右子树的深度
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)

        #3. 本级递归做什么，返回左右子树的最大深度+1
        return max(leftDepth, rightDepth) + 1

s = Solution3()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(s.maxDepth(root))