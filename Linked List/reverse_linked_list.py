class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next


class Solution:
    @staticmethod
    def reverse_list(head: ListNode) -> ListNode:
        prev_node = None
        current_node = head

        while current_node:
            next_node = current_node.next

            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        return prev_node


if __name__ == '__main__':
    list1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    list2 = ListNode(1, ListNode(2))
    list3 = ListNode(0)

    result1 = Solution.reverse_list(list1)
    print(result1)

    result2 = Solution.reverse_list(list2)
    print(result2)

    result3 = Solution.reverse_list(list3)
    print(result3)
