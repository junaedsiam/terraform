"""
Problem description: 
---------
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
"""
# Helpers


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


def reverse_linked_list(head):
    if not head:
        return None

    prev_node = None
    curr_node = head

    while curr_node:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node

    return prev_node


def reverse_linked_list_recurse(curr, prev=None):
    if not curr:
        return prev
    next = curr.next
    curr.next = prev
    return reverse_linked_list_recurse(next, curr)


if __name__ == '__main__':
    head = create_ll_from_list([1, 2, 3, 4, 5])
    print_ll(reverse_linked_list(head))
    head = create_ll_from_list([1, 2, 3, 4, 5])
    print_ll(reverse_linked_list_recurse(head))
