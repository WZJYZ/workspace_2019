'''
有序合并K个链表
思路1：先合并两个，再一个加一个的合并, 结果超出时间限制
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


'''

class Solution:
    def mergeKLists(self, lists):

        def mergeTwoLinks(link1, link2):
            head = ListNode(-1)
            cur = head
            while link1 and link2:

                if link1.val < link2.val:
                    tmp = ListNode(link1.val)
                    cur.next = tmp
                    cur = cur.next
                    link1 = link1.next
                elif link1.val > link2.val:
                    tmp = ListNode(link2.val)
                    cur.next = tmp
                    cur = cur.next
                    link2 = link2.next
                else:
                    tmp1 = ListNode(link1.val)
                    tmp2 = ListNode(link2.val)
                    tmp1.next = tmp2
                    cur.next = tmp1
                    cur = cur.next.next
                    link1 = link1.next
                    link2 = link2.next
            if link1:
                cur.next = link1
            if link2:
                cur.next = link2
            return head
        if len(lists) == 0:
            return []

        while len(lists) > 1:
            a = lists.pop()
            b = lists.pop()
            tmp =  mergeTwoLinks(a, b).next
            lists.append(tmp)

        return lists[0]

'''
class Solution:
    def mergeKLists1(self, lists):
        def mergeTwoLinks(link1, link2):
            if link1 is None:
                return link2
            if link2 is None:
                return link1
            if link1.val <= link2.val:
                link1.next = mergeTwoLinks(link1.next, link2)
                return link1
            else:
                link2.next = mergeTwoLinks(link1, link2.next)
                return link2

        if len(lists) == 0:
            return []

        while len(lists) > 1:
            a = lists.pop()
            b = lists.pop()
            tmp = mergeTwoLinks(a, b)
            lists.append(tmp)
        return lists[0]

    def mergeKLists2(self, lists): #把链表都加入一个数组中，然后排序，再加到最后的链表中

        res = []

        for l in lists:
            while l:
                res.append(l.val)
                l = l.next
        if res == []:
            return []
        res.sort()
        head = ListNode(-1)
        cur = head
        for i in res:
            cur.next = ListNode(i)
            cur = cur.next
        return head.next

    def mergeKLists(self, lists): #使用最小堆实现
        import heapq

        result = ListNode(-1)
        cur = result

        p = []
        x = 0

        for i in lists:
            while i:
                heapq.heappush(p, (i.val, x, i))
                i = i.next
                x += 1
        while p:
            cur.next = heapq.heappop(p)[1]
            cur = cur.next
        return result.next


s = Solution()
a = ListNode(1)
a.next = ListNode(4)
a.next.next = ListNode(5)

b = ListNode(1)
b.next = ListNode(3)
b.next.next = ListNode(4)

c = ListNode(2)
c.next = ListNode(6)

head = s.mergeKLists([a, b, c])

while head:
    print(head.val)
    head = head.next