def check_prime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


if __name__ == '__main__':
    print(check_prime(2))
    print(check_prime(3))
    print(check_prime(11))
    print(check_prime(18))
    print(check_prime(27))
