"""
Problem description: 
---------
You have a 32-bit unsigned integer called 'num' and another integer call 'i'. You need to perform following
1. Get the bit value at the "i"th position of "num"
2. Set the bit value at the "i"th position of "num"
3. Clear the bit at the "i"th position of "num"
"""


def get(num, i):
    # 1. Get the bit value at the "i"th position of "num"
    return (num >> i - 1) & 1


def set(num, i):
    # 2. Set the bit value at the "i"th position of "num"
    return num | (1 << i - 1)


def clear(num, i):
    # 3. Clear the bit at the "i"th position of "num"
    return num & ~(1 << i - 1)


if __name__ == '__main__':
    print(get(25, 3))
    print(set(25, 3))
    print(clear(29, 3))
