# Brute force
# Time complexity: O(n / 2 ) -> O(n), Space complexity: O(1)
def print_all_divisors_brute(num):
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            print(i, end=" ")
    print(num)

# Better approach
# The quotient of a Dividend by one of the divisors is actually another divisor of that dividend.
# Like, 4 divides 36. The quotient is 9, and 9 also divides 36
# And you only have to traverse till sqrt(num) to find all the divisors
# Time complexity: O(sqrt(N)), Space complexity: O(1)


def print_all_divisors(num):
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            print(i, end=" ")
            if i != num // i:
                print(num//i, end=" ")
    print()


if __name__ == '__main__':
    print_all_divisors_brute(36)
    print_all_divisors_brute(11)
    print_all_divisors(36)
    print_all_divisors(11)
