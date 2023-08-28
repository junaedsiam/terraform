"""
Problem description: 
---------
You are given two strings 'A' and 'B' of length 'N' and 'M\' respectively.
Return the string that has more distinct subsequences, if both strings have the same number of distinct subsequences, then return 'A'.

Example 1:
-----
Input: "ab", "dd"
Output: "ab"
Explanation: 'A' has distinct subsequences = ["a", "b", "ab"],
'B' has distinct subsequences = ["d", "dd"]
so our answer is "ab"

Example 2:
----
Input: "abc", "dddd"
Output: "abc"
"""


def more_subsequence(a, b):
    # Time complexity:
    # Since the problem does not require the actual subsequences but rather asks
    # for the string with more subsequences (count), we can determine this by considering
    # the number of distinct characters. The string with a higher count of distinct characters
    # will have more subsequences.
    n = len(a)
    m = len(b)
    ht = {}
    for char in a:
        if char in ht:
            ht[char] += 1
        else:
            ht[char] = 1
    a_count = len(ht.keys())
    ht.clear()
    for char in b:
        if char in ht:
            ht[char] += 1
        else:
            ht[char] = 1
    b_count = len(ht.keys())

    if a_count == b_count:
        return a if n >= m else b
    return a if a_count > b_count else b


if __name__ == '__main__':
    ex_1, ex_2 = ["ab", "dd"], ["dcfba", "fhfe"]
    print(more_subsequence(ex_1[0], ex_1[1]))
    print(more_subsequence(ex_2[0], ex_2[1]))
