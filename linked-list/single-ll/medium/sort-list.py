"""
Problem description: 
---------
Given the head of a linked list, return the list after sorting it in ascending order.

Example 1:
------------
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:
----------
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Example 3:
--------
Input: head = []
Output: []

Constraints:
---------
The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105
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

# Actual Code


def merge(l1, l2):
    dummy = ListNode(0)
    curr = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            dummy.next = l1
            l1 = l1.next
        else:
            dummy.next = l2
            l2 = l2.next

        dummy = dummy.next
    while l1:
        dummy.next = l1
        dummy = dummy.next
        l1 = l1.next
    while l2:
        dummy.next = l2
        dummy = dummy.next
        l2 = l2.next

    return curr.next


def sort_list(head):
    # Time complexity: O(n log n)
    if not head or not head.next:
        return head

    tmp = None
    # find the middle node
    fast = slow = head
    while fast and fast.next:
        tmp = slow
        slow = slow.next
        fast = fast.next.next
    # Detaching first half from the linked list
    tmp.next = None
    # Sort the first half
    l1 = sort_list(head)
    # Sort the second half
    l2 = sort_list(slow)
    # merge them: TODO: might need to adjust this later
    return merge(l1, l2)


if __name__ == '__main__':
    head = create_ll_from_list([5, 4, 3, 2, 1])
    print_ll(sort_list(head))
