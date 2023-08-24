from typing import List
"""
Problem description: 
---------
Reverse a given stack of 'N' integers using recursion. You are required to make changes in the input parameter itself. 
Note: You are not allowd to use any extra space other than the internal stack space used due to recursion.
Example: 
Input: [1,2,3,4,5]
Output: [5,4,3,2,1]
"""


def reverse_a_stack(stack: List[int]):
    if not len(stack):
        return
    val = stack.pop()
    reverse_a_stack(stack)
    stack.insert(0, val)


if __name__ == '__main__':
    stack = [1, 2, 3, 4, 5]
    reverse_a_stack(stack)
    print(stack)
