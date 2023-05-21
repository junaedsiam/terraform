def reverseInteger(n):
    is_positive = n >= 0
    res = 0
    curr = n if is_positive else -1 * n

    while curr != 0:
        rem = curr % 10
        res = res*10 + rem
        curr //= 10
    return res if is_positive else -1 * res


if __name__ == '__main__':
    print(reverseInteger(123))
    print(reverseInteger(9))
    print(reverseInteger(-123))
