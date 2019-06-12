# Definition for a binary tree node.
class TreeNode:

    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None

class Solution1:
    #BFS
    def levelOrder(self, root: TreeNode):
        '''

        :param root:
        :return:List[List[int]]
        '''
        import collections
        if not root:
            return []

        result = []
        queue = collections.deque()
        queue.append(root)

        #visited = set(root)

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(current_level)

        return result


class Solution2:
    #dfs
    def levelOrder(self, root: TreeNode):
        '''

        :param root:
        :return:List[List[int]]
        '''
        if not root:
            return []
        self.result = []
        self._dfs(root, 0)
        return self.result

    def _dfs(self, root, level):
        if not root:
            return
        if len(self.result) < level + 1:
            self.result.append([])

        self.result[level].append(root.val)
        self._dfs(root.left, level+1)
        self._dfs(root.right, level+1)
class Solution3:
    #BFS
    def levelOrder(self, root: TreeNode):
        '''

        :param root:
        :return:List[List[int]]
        '''
        import collections
        result = []
        if not root:
            return []
        queue = collections.deque()
        queue.append((root, 0))

        while queue:
            temp = queue.popleft()
            node = temp[0]
            level = temp[1]

            if level == len(result):
                result.append([])

            result[level].append(node.val)

            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))

        return result


s = Solution3()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(s.levelOrder(root))