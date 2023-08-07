"""
Problem description: 
---------
You will be given roman string, convert it to integer. Will be given integer, convert it to roman.
"""


def roman_to_int(s):
    # Time complexity: O(n), Space Complexity: O(1)
    hash = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    n = len(s)
    num = hash[s[n - 1]]
    for i in range(n-2, -1, -1):
        if hash[s[i]] < hash[s[i + 1]]:
            num -= hash[s[i]]
        else:
            num += hash[s[i]]
    return num


def int_to_roman(num):
    # Time complexity: O(n), Space Complexity: O(1)
    limits = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romans = ['M', 'CM', 'D', 'CD', 'C', 'XC',
              'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    res = ''
    idx = 0
    while num:
        if num >= limits[idx]:
            res += romans[idx]
            num -= limits[idx]
        else:
            idx += 1
    return res


if __name__ == '__main__':
    # Roman to Integer
    ex_1, ex_2, ex_3 = 'III', 'LVIII', 'MCMXCIV'
    print(roman_to_int(ex_1))
    print(roman_to_int(ex_2))
    print(roman_to_int(ex_3))
    # Integer to Roman
    ex_1, ex_2, ex_3 = 3, 58, 1994
    print(int_to_roman(ex_1))
    print(int_to_roman(ex_2))
    print(int_to_roman(ex_3))
