def evenlyDivides(n):
    curr = n
    count = 0
    while curr:
        rem = curr % 10
        if rem != 0 and n % rem == 0:
            count += 1
        curr //= 10
    return count


if __name__ == '__main__':
    print(evenlyDivides(12))
    print(evenlyDivides(23))
    print(evenlyDivides(236))
    print(evenlyDivides(100))
