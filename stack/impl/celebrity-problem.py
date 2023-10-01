"""
Problem description: 
---------
A celebrity is a person who is known to all but does not know anyone at a party. If you go to a party of N people, find if there is a celebrity in the party or not.
A square NxN matrix M[][] is used to represent people at the party such that if an element of row i and column j  is set to 1 it means ith person knows jth person. Here M[i][i] will always be 0.
Note: Follow 0 based indexing.
Follow Up: Can you optimize it to O(N)
 

Example 1:

Input:
N = 3
M[][] = {{0 1 0},
         {0 0 0}, 
         {0 1 0}}
Output: 1
Explanation: 0th and 2nd person both
know 1. Therefore, 1 is the celebrity. 

Example 2:

Input:
N = 2
M[][] = {{0 1},
         {1 0}}
Output: -1
Explanation: The two people at the party both
know each other. None of them is a celebrity.

Your Task:
You don't need to read input or print anything. Complete the function celebrity() which takes the matrix M and its size N as input parameters and returns the index of the celebrity. If no such celebrity is present, return -1.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)


Constraints:
2 <= N <= 3000
0 <= M[][] <= 1
"""


# Helper
def knows(mat, a, b):
    return mat[a][b]


def celebrity_problem(mat, n):
    stack = []
    # Insert all elements in the stack
    for i in range(n):
        stack.append(i)

    # Pop out two elements at a time and check who knows, and put one back into the stack
    while len(stack) > 1:
        a = stack.pop()
        b = stack.pop()

        if knows(mat, a, b):
            stack.append(b)
        else:
            stack.append(a)
    # Finally you should be left with one element
    candidate = stack.pop()
    # check the row for the candidate
    # If the candidate is a celebrity then all the elements in the row will be 0
    for item in mat[candidate]:
        if item != 0:
            return -1

    # check the col for the candidate
    # If all the elements in the col is not 1, except the candidate itself, candidate is not celebrity
    for i in range(n):
        if i != candidate and mat[i][candidate] != 1:
            return -1

    return candidate


if __name__ == '__main__':
    print(celebrity_problem([[0, 1, 0], [0, 0, 0], [0, 1, 0]], 3))
