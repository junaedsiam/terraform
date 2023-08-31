"""
Problem description: 
---------
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:
----------
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
--------
Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:
------------
0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""

ht = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


def solve(digits, idx, combo, res):
    if idx == len(digits):
        res.append(combo)
        return

    letters = ht[digits[idx]]

    for letter in letters:
        solve(digits, idx + 1, combo + letter, res)


def letter_combination_of_phone_number(digits: str):
    # Time complexity: n ^ m
    if not digits:
        return []
    res = []
    solve(digits, 0, "", res)
    return res


if __name__ == '__main__':
    ex_1, ex_2 = "23", "2"
    print(letter_combination_of_phone_number(ex_1))
    print(letter_combination_of_phone_number(ex_2))
