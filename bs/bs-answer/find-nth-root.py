import math


def multiply(num, times):
    ans = 1.0
    for i in range(times):
        ans = ans * num

    return ans


def find_nth_root(n, num):
    # Time complexity: O(log(n)), Space complexity: O(1)
    low = 0
    high = num / 2.0
    eps = 1e-7

    while (high - low) > eps:
        mid = (low + high) / 2.0
        res = multiply(mid, n)
        if res < num:
            low = mid
        else:
            high = mid
    # Round the result if it crosses 5+9
    if math.ceil(low) - low <= 0.00009:
        low = math.ceil(low)

    return low


if __name__ == '__main__':
    print(find_nth_root(3, 27))  # ~ Precisely 3
    print(find_nth_root(3, 8))  # ~ Precisely 2
