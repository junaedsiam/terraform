"""
Problem description: 
---------
Delete a node of a linked list without its predecessor
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def print_ll(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(",".join([str(x) for x in res]))


def delete_node_without_predecessor(node):
    node.val = node.next.val
    node.next = node.next.next


if __name__ == '__main__':
    ll = ListNode(4)
    ll.next = ListNode(5)
    ll.next.next = ListNode(1)
    ll.next.next.next = ListNode(9)
    delete_node_without_predecessor(ll.next)
    print_ll(ll)
