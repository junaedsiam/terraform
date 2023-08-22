"""
Problem description: 
---------
Given the head of a linked list, rotate the list to the right by k places.

Example 1:
--------
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
--------
Input: head = [0,1,2], k = 4
Output: [2,0,1]
 
Constraints:
-------
The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
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


def get_ll_length(head):
    counter = 0
    curr = head
    while curr:
        counter += 1
        curr = curr.next
    return counter


def rotate_list(head, k):
    n = get_ll_length(head)
    r_length = k % n

    while not n or not r_length or k == 0:
        return head

    prev = None
    curr = head
    for _ in range(n - r_length):
        prev = curr
        curr = curr.next

    # Detaching the rotation point
    prev.next = None
    new_head = curr
    while curr.next:
        curr = curr.next

    curr.next = head

    return new_head


if __name__ == '__main__':
    head = create_ll_from_list([1, 2, 3, 4, 5])
    print_ll(rotate_list(head, 2))
