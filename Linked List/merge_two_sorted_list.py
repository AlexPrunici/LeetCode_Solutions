class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next


class Solution:
    @staticmethod
    def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1

        result = tail = ListNode()

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        tail.next = l1 or l2

        return result.next


if __name__ == '__main__':
    _list1 = ListNode(1, ListNode(2, ListNode(4)))
    _list2 = ListNode(1, ListNode(3, ListNode(4)))

    _list3 = ListNode()
    _list4 = ListNode(0)

    result1 = Solution.merge_two_lists(_list1, _list2)
    print(result1)

    result2 = Solution.merge_two_lists(_list3, _list4)
    print(result2)
