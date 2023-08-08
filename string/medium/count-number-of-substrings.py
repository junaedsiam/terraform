"""
Problem description: 
---------
You are given a string 'str' of lowercase alphabets and an integer 'k' .

Your task is to return the count all the possible substrings that have exactly 'k' distinct characters.
Example 1:
---------
str = aacfssa
k = 3
Output:
----
5    
Explanation:
-----------
Given 'str' = “aacfssa”. We can see that the substrings with only 3 distinct characters are {aacf, acf, cfs, cfss, fssa}. 

Therefore, the answer will be 5.
Example 2:
----------
str = qffds
k = 4

Output:
-----
1

Constraints:
-----------
1 <= |str| <= 10^5
1 <= k <= 26

"""


def count_number_of_substrings(s, k):
    # Time complexity: O(n ^ 2), Space complexity: O(1)
    res = 0
    for i in range(len(s)):
        ht = [0] * 26
        count = 0
        for j in range(i, len(s)):
            idx = ord(s[j]) - ord('a')
            if ht[idx] == 0:
                count += 1
            ht[idx] += 1
            if count == k:
                res += 1
            if count > k:
                break
    return res


if __name__ == '__main__':
    ex_1, ex_2 = ("aacfssa", 3), ("qffds", 4)
    print(count_number_of_substrings(ex_1[0], ex_1[1]))
    print(count_number_of_substrings(ex_2[0], ex_2[1]))
