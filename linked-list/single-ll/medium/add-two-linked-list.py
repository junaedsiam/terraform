"""
Problem description: 
---------
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
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


def add_two_linked_list(l1, l2):
    carry = 0
    dummy = ListNode(0)
    tmp = dummy
    while l1 or l2 or carry:
        sum = 0
        if l1:
            sum += l1.val
            l1 = l1.next

        if l2:
            sum += l2.val
            l2 = l2.next
        sum += carry
        carry = sum // 10
        tmp.next = ListNode(sum % 10)
        tmp = tmp.next

    return dummy.next


if __name__ == '__main__':
    l1 = create_ll_from_list([2, 4, 3])
    l2 = create_ll_from_list([5, 6, 4])
    print_ll(add_two_linked_list(l1, l2))
    l1 = create_ll_from_list([9, 9, 9, 9, 9, 9, 9])
    l2 = create_ll_from_list([9, 9, 9, 9])
    print_ll(add_two_linked_list(l1, l2))
