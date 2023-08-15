"""
Problem description: 
---------
Given the head of a singly linked list, return true if it is a 
palindrome
 or false otherwise.


Example 1:

Input: head = [1,2,2,1]
Output: true

Example 2:

Input: head = [1,2]
Output: false

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 

Follow up: Could you do it in O(n) time and O(1) space?
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


def reverse_list(node):
    prev = None
    curr = node
    next = None

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev


def check_if_the_list_palindrome(head):
    # Edge case
    if not head or not head.next:
        return True

    fast = slow = head
    # Find the second last index from the middle
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    # Middle starts from slow.next. Reverse the list from there
    slow.next = reverse_list(slow.next)
    # put slow in starting of second half
    slow = slow.next

    # now start another pointer from the beginning and compare node vals.
    entry = head
    while slow != None:
        if slow.val != entry.val:
            # if does not match return false
            return False
        slow = slow.next
        entry = entry.next
    return True


if __name__ == '__main__':
    head = create_ll_from_list([1, 2, 3, 2, 1])
    head2 = create_ll_from_list([1, 2, 3])
    print(check_if_the_list_palindrome(head))
    print(check_if_the_list_palindrome(head2))
