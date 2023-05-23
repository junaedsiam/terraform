"""
Armstrong Numbers are the numbers having the sum of digits raised to power no. of digits is equal to a given number. Examples- 0, 1, 153, 370, 371, 407, and 1634 are some of the Armstrong Numbers.
"""


def armstrong_number(n):
    # First count the digit of the number
    count = 0
    curr = n
    while curr:
        curr //= 10
        count += 1
    # Then take each digit and powered it by the digit count and sum it up
    curr = n
    res = 0

    while curr:
        rem = curr % 10
        res += rem ** count
        curr //= 10
    return True if res == n else False


if __name__ == '__main__':
    print(armstrong_number(153))
    print(armstrong_number(1634))
    print(armstrong_number(1635))
