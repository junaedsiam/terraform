"""
Problem description: 
--------
You are given a doubly-linked list of size 'N', consisting of positive integers. Now your task is to reverse it and return the head of the modified list.

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None


def print_ll(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(",".join([str(x) for x in res]))


def reverse_double_ll(head):
    if not head.next:
        return head

    while head:
        new_head = head
        prev = head.prev
        next = head.next
        head.next = prev
        head.prev = next
        head = next
    return new_head


if __name__ == '__main__':
    ll1 = ListNode(4)
    ll2 = ListNode(3)
    ll3 = ListNode(2)
    ll4 = ListNode(1)
    ll1.next = ll2
    ll2.prev = ll1
    ll2.next = ll3
    ll3.prev = ll2
    ll3.next = ll4
    ll4.prev = ll3
    print_ll(reverse_double_ll(ll1))
