"""
Problem description: 
---------
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:
----
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:
---
Input: heights = [2,4]
Output: 4
 

Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104
"""


def largest_rectangle_in_a_histogram(heights):
    # Time Complexity: O(n)
    n = len(heights)
    stack = []
    # pse: previous smallest elements for every element
    pse = [0] * n
    for i in range(n):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        idx = (stack[-1] + 1) if stack else 0
        pse[i] = idx
        stack.append(i)
    # Empty the stack before generating next smallest elements
    stack = []
    # nse: next smallest elements for every element
    nse = [0] * n
    for i in range(n - 1, -1, -1):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        idx = (stack[-1] - 1) if stack else n - 1
        nse[i] = idx
        stack.append(i)
    # rectangle area theorem is -> (nse - pse + 1) * heights[i]
    res = -2**31
    for i in range(n):
        res = max(res, (nse[i] - pse[i] + 1) * heights[i])
    # return max among all the rectangle areas
    return res


if __name__ == '__main__':
    print(largest_rectangle_in_a_histogram([2, 1, 5, 6, 2, 3]))
    print(largest_rectangle_in_a_histogram([2, 4]))
