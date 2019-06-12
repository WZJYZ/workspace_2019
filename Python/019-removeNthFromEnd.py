'''
思路1：将链表保存为list，删除倒数第n个值，再将list转换为链表
思路2：双指针法，快慢指针相差为n
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def reverse(self, link):
        dummy = ListNode(-1)

        while link:
            tmp = ListNode(link.val)
            tmp.next = dummy.next
            dummy.next = tmp
            link = link.next
        return dummy

    def removeNthFromEnd1(self, head, n):
        tmp = []
        while head:
            tmp.append(head.val)
            head = head.next

        del tmp[len(tmp) - n]
        head = res = ListNode(-1)
        for i in tmp:
            cur = ListNode(i)
            res.next = cur
            res = res.next
        return head.next
    def removeNthFromEnd(self, head, n):
        slow = fast = dummy = ListNode(-1)
        dummy.next = head
        for i in range(n):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        return dummy.next



if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l1.next = l2
    l2.next = l3

    s = Solution()
    h = s.removeNthFromEnd(l1, 3)
    while h:
        print(h.val)
        h = h.next