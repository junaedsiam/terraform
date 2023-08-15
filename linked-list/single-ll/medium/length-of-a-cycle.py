
"""
Problem Description:
-------
You're given a linked list. The last node might point to null,
or it might point to a node in the list, thus forming a cycle.
Find out whether the linked list has a cycle or not , and the length of the cycle if it does.
If there is no cycle, return 0, otherwise return the length of the cycle.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_ll_from_list(nums):
    head = None
    prev = None
    for num in nums:
        curr = ListNode(num)
        if not head:
            head = curr
            prev = curr
            continue
        prev.next = curr
        prev = curr
    return head, prev


def length_of_cycle(head: ListNode) -> int:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        # have to check if fast node reaches the end
        if fast == slow:
            count = 1
            slow = slow.next
            while slow != fast:
                slow = slow.next
                count += 1
            return count
    return 0


if __name__ == '__main__':
    head, tail = create_ll_from_list([1, 2, 3, 4, 5, 6, 7])
    cycle_node = head.next.next
    tail.next = cycle_node
    head_2, tail_2 = create_ll_from_list([1, 2, 3])
    print(length_of_cycle(head))
    print(length_of_cycle(head_2))
