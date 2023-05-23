def check_palindrome(n):
    """
    102
    curr -> 10, rem -> 2, reverse -> 0 * 10 + 2
    curr -> 1 , rem -> 0, reverse -> 2 * 10 + 0
    curr -> 0 , rem -> 1, reverse -> 20 * 10 + 1
    """
    curr = n
    rev_n = 0

    while curr:
        rem = curr % 10
        curr //= 10
        rev_n = rev_n * 10 + rem

    return True if rev_n == n else False


if __name__ == '__main__':
    print(check_palindrome(101))
    print(check_palindrome(9))
    print(check_palindrome(102))
