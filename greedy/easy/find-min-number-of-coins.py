"""
Problem description: 
---------
Given an infinite supply of Indian currency valued coins and an amount 'N'. Find the minimum conis needed to make the sum equal to 'N'. You have to return the list containing the value of coins required in decerasing order.
Input: 13
Ouput: [10, 2, 1]
"""


def find_min_number_of_coins(n):
    # Time complexity:
    notes = [1000, 500, 100, 50, 20, 10, 5, 2, 1]
    res = []
    idx = 0
    while n:
        if notes[idx] > n:
            idx += 1
            continue
        n -= notes[idx]
        res.append(notes[idx])

    return res


if __name__ == '__main__':
    print(find_min_number_of_coins(13))
