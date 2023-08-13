"""
Problem description: 
---------
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
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


def find_middle_node(head):
    # Time complexity:
    if not head.next:
        return head

    slow = head
    fast = head.next

    while slow and fast:
        print('slow', slow.val, 'fast', fast.val)
        slow = slow.next
        fast = fast.next.next if fast.next else None
    return slow


if __name__ == '__main__':
    head = create_ll_from_list([1, 2, 3, 4, 5, 6])
    head2 = create_ll_from_list([1, 2, 3, 4, 5])

    # print(head)
    # print_ll(head)
    print_ll(find_middle_node(head))
    print_ll(find_middle_node(head2))
