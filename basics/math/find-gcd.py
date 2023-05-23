# This is a brute force approach of finding Greatest Common Divisor (GCD) of two numbers
# Time complexity : O(N), Space complexity: O(1)

def find_gcd_brute_force(num1, num2):
    for i in range(min(num1, num2), 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i


# This is the euclidean approarch to find GCD.
# Time complexity: O(log(min(num1,num2))) # Space complexity: O(1)

def find_gcd(num1, num2):
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    return gcd(num1, num2) if num1 > num2 else gcd(num2, num1)


if __name__ == '__main__':
    print(find_gcd_brute_force(10, 5))
    print(find_gcd_brute_force(11, 13))
    print(find_gcd_brute_force(20, 15))
    print(find_gcd(10, 5))
    print(find_gcd(11, 13))
    print(find_gcd(20, 15))
