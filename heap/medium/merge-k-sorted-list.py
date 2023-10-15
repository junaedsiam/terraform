"""
Problem description: 
---------
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
"""
from queue import PriorityQueue


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


def merge_k_sorted_list(lists):
    dummy = ListNode(None)
    curr = dummy
    q = PriorityQueue()

    for i in range(len(lists)):
        node = lists[i]
        if node:
            q.put((node.val, i, node))

    while q.qsize():
        i += 1
        curr.next = q.get()[2]
        curr = curr.next
        if curr.next:
            q.put((curr.next.val, i, curr.next))

    return dummy.next


if __name__ == '__main__':
    lists = [create_ll_from_list(ll) for ll in [[1, 4, 5], [1, 3, 4], [2, 6]]]
    print_ll(merge_k_sorted_list(lists))
