"""
Problem description: 
---------

"""
from collections import defaultdict


class ListNode:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


def print_ll(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(",".join([str(x) for x in res]))


def print_ll_with_random(head):
    res = []
    while head:
        res.append('curr')
        res.append(head.val)
        res.append('random')
        res.append(head.random.val)
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


def clone_linked_list_with_random_pointer(head):
    # step 1: Create a copy of each node and keep them in the next node
    curr = head
    while curr:
        new_node = ListNode(curr.val)
        new_node.next = curr.next
        curr.next = new_node
        curr = curr.next.next

    # step 2: connect copy to its random copy
    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next

    # step 3: Seperate the original and clone list
    # This is a hard one to pull off
    dummy = ListNode(0)
    curr = head
    tmp = dummy

    while curr:
        tmp.next = curr.next
        curr.next = curr.next.next
        tmp = tmp.next
        curr = curr.next

    return dummy.next


def clone_linked_list_with_random_pointer_ht(head):
    ht = defaultdict()
    # first create a copy of all existing nodes and save it in ht
    curr = head
    while curr:
        clone = ListNode(curr.val)
        ht[curr] = clone
        curr = curr.next

    # secondly attach the next and random accordingly
    curr = head

    while curr:
        ht[curr].next = ht[curr.next]
        ht[curr].random = ht[curr.random]
        curr = curr.next

    return ht[head]


if __name__ == '__main__':
    head = create_ll_from_list([1, 2, 3, 4, 5])
    h1 = head
    h2 = head.next
    h3 = head.next.next
    h4 = head.next.next.next
    h5 = head.next.next.next.next
    h1.random = h3
    h2.random = h4
    h3.random = h5
    h4.random = h1
    h5.random = h2
    head2 = clone_linked_list_with_random_pointer(head)
    # detaching the head from other node in the original list to test the cloned list
    head.next = None
    print_ll_with_random(head)
    print_ll_with_random(head2)
