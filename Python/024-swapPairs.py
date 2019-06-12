class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    # 1. 迭代方法
    def swapPairs(self, head):
        dummy = ListNode(-1)
        dummy.next = head

        pre = dummy
        while pre.next and pre.next.next:
            node1 = pre.next
            node2 = node1.next
            lat = node2.next

            pre.next = node2
            node2.next = node1
            node1.next = lat

            pre = node1

        return dummy.next

        return dummy.next


class Solution2:
    # 2. 递归方法
    def swapPairs(self, head):
        # 1.终止条件，链表为空或只有一个节点，没得交换
        #if not head or not head.next:
        if (head is None) or (head.next is None):
            return head
        # 一共三个节点:head, next_node, swapPairs(next.next)
        # 下面的任务便是交换这3个节点中的前两个节点
        next_node = head.next
        head.next = self.swapPairs(next_node.next)
        next_node.next = head

        # 根据第二步：返回给上一级的是当前已经完成交换后，即处理好了的链表部分
        return next_node


a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
a.next.next.next = ListNode(4)
s = Solution2()
head = s.swapPairs(a)
while head:
    print(head.val)
    head = head.next