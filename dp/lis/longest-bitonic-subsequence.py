"""
Problem URL: https://www.codingninjas.com/studio/problems/longest-bitonic-sequence_1062688
---------

Problem Description:
---------

A Bitonic Sequence is a sequence of numbers that is first strictly increasing and then strictly decreasing.


A strictly ascending order sequence is also considered bitonic, with the decreasing part as empty, and same for a strictly descending order sequence.



For example, the sequences [1, 3, 5, 3, 2], [1, 2, 3, 4] are bitonic, whereas the sequences [5, 4, 1, 4, 5] and [1, 2, 2, 3] are not.



You are given an array 'arr' consisting of 'n' positive integers.



Find the length of the longest bitonic subsequence of 'arr'.



Example :
Input: 'arr' = [1, 2, 1, 2, 1]

Output: 3

Explanation: The longest bitonic subsequence for this array will be [1, 2, 1]. Please note that [1, 2, 2, 1] is not a valid bitonic subsequence, because the consecutive 2's are neither strictly increasing, nor strictly decreasing.
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1 :
5 
1 2 1 2 1


Sample Output 1:
3


Explanation For Sample Input 1:
The longest bitonic subsequence for this array will be [1, 2, 1]. Please note that [1, 2, 2, 1] is not a valid bitonic subsequence, because the consecutive 2's are neither strictly increasing, nor strictly decreasing.


Sample Input 2 :
5
1 2 1 3 4


Sample Output 2 :
4


Explanation For Sample Input 2:
The longest bitonic sequence for this array will be [1, 2, 3, 4].


Expected time complexity :
The expected time complexity is O(n ^ 2).


Constraints:
1 <= 'n' <= 10^3
1 <= 'arr[i]' <= 10^5

Time Limit: 1sec
"""
from typing import List


def longest_bitonic_subsequence(arr: List[int], n: int) -> int:
    '''
    # Time complexity: O(n ^ 2)
    # Space complexity: O(2n)
    Intuition is to use the same principle that we have used
    in solving Largest increasing subsequence. For bitonic, we have to do it twice
    from 0 to n - 1
    and from n - 1 to 0 (reverse)
    Now each index i, in both dp row contains longest increasing from 0 -> n - 1
    and longest increasing from n - 1 -> 0, which is decreasing in reverse
    Finally add them both up in reverse order,
    and you will get longest bitonic subseq
    '''
    dp1 = [1] * n
    dp2 = [1] * n

    # find lis from 0 to n - 1
    for i in range(n):
        for prev_i in range(i):
            if arr[i] > arr[prev_i] and 1 + dp1[prev_i] > dp1[i]:
                dp1[i] = 1 + dp1[prev_i]

    # find lis from n - 1 to 0
    for i in range(n - 1, -1, -1):
        for prev_i in range(n - 1, i, -1):
            if arr[i] > arr[prev_i] and 1 + dp2[prev_i] > dp2[i]:
                dp2[i] = 1 + dp2[prev_i]

    # find the max
    max_i = 0

    for i in range(n):
        max_i = max(max_i, dp1[i] + dp2[i] - 1)

    return max_i


if __name__ == '__main__':
    print(longest_bitonic_subsequence([1, 2, 1, 3, 4]))
