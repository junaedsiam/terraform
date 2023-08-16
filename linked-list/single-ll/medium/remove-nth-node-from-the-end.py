"""
Problem description: 
---------
Given a linked list, and a number N. Find the Nth node from the end of this linked list and delete it. Return the head of the new modified linked list.

Example 1 : 

Input: head = [1,2,3,4,5], n = 2

Output: [1,2,3,5]

Example 2:

Input: head = [7,6,9,4,13,2,8], n = 6

Output: [7,9,4,13,2,8]
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_ll(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(",".join([str(x) for x in res]))


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
    return head

# Two pointer one


def remove_nth_node_from_the_end(head, n):
    p1 = p2 = head
    k = 1

    while p1.next:
        if k > n:
            p2 = p2.next
        p1 = p1.next
        k += 1

    if p2 == head and k == n:
        head = head.next
    else:
        p2.next = p2.next.next

    return head

# Two pointer two


def remove_nth_node_from_the_end_two(head, n):
    start = ListNode()
    start.next = head
    fast = start
    slow = start

    for _ in range(n):
        fast = fast.next

    while fast.next != None:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next

    return start.next


if __name__ == '__main__':
    head = create_ll_from_list([1, 2, 3, 4, 5])
    print_ll(remove_nth_node_from_the_end(head, 2))
    head = create_ll_from_list([1, 2, 3, 4, 5])
    print_ll(remove_nth_node_from_the_end_two(head, 2))
