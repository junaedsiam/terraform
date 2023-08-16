"""
Problem description: 
---------
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Example 1:
---------
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:
---------
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
 

Constraints:

The number of nodes in the linked list is in the range [0, 104].
-106 <= Node.val <= 106
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


def odd_even_linked_list(head):
    if not head or not head.next or not head.next.next:
        return head

    odd = head
    even = head.next
    even_start = head.next

    while odd.next and even.next:
        odd.next = even.next
        even.next = odd.next.next
        odd = odd.next
        even = even.next

    odd.next = even_start

    return head


if __name__ == '__main__':
    head = create_ll_from_list([1, 2, 3, 4, 5, 6, 7])
    head = odd_even_linked_list(head)
    print_ll(head)
