"""
Problem description: 
---------
You are given a stack 'S'. Your task is to recursively sort the stack. For example 

Input: elements present in stack from top to bottom -3 14 18 -5 30
Output: 30 18 14 -3 -5
Explanation: The given stack is sorted know 30 > 18 > 14 > -3 > -5

Input: elements present in stack from top to bottom 1 2 3
Output: 3 2 1
Explanation: The given stack is sorted know 3 > 2 > 1
"""


def insert(stack, elem):
    if len(stack) == 0 or elem > stack[-1]:
        stack.append(elem)
        return
    else:
        top = stack.pop()
        insert(stack, elem)
        stack.append(top)


def sort_a_stack(stack):
    # Time complexity: O(n ^ 2)
    if not len(stack):
        return
    elem = stack.pop()
    sort_a_stack(stack)
    insert(stack, elem)


if __name__ == '__main__':
    stack = [3, 2, 1, 4, 5]  # 5,4,3,2,1
    sort_a_stack(stack)
    print(stack)
