"""
Problem description: 
---------
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

Example 1:
----------
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
----------
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
----------
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
    return head, prev


def get_entry_node(head):
    slow = head
    fast = head
    entry = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        # have to check if fast node reaches the end
        if fast == slow:
            while slow:
                slow = slow.next
                entry = entry.next
                if slow == entry:
                    return entry
    return None


def starting_point_of_loop_in_a_linked_list(head):
    # Time complexity:
    # Strategy is to run two seperate pointers (slow and fast) to eventually reach the starting point of loop.
    # When fast pointer will reach the end, another "entry" pointer will start its journey from the head
    # And when the slow pointer will reach the end, you will get the starting point of the cycle in entry node
    slow = fast = entry = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        # have to check if fast node reaches the end
        if fast == slow:
            while slow != entry:
                slow = slow.next
                entry = entry.next
            return slow
    return None


if __name__ == '__main__':
    head, tail = create_ll_from_list([1, 2, 3, 4, 5, 6, 7])
    cycle_node = head.next.next
    tail.next = cycle_node
    head_2, tail_2 = create_ll_from_list([1, 2, 3])
    node = starting_point_of_loop_in_a_linked_list(head)
    print(node.val)
    node = starting_point_of_loop_in_a_linked_list(head_2)
    print(node)
