"""
Problem description: 
---------

"""


def power_of_two(n):
    return n & n - 1 == 0


if __name__ == '__main__':
    print(power_of_two(16))
    print(power_of_two(14))
