"""
Problem description: 
---------
You are the owner of a Shipment company. You use conveyor belts to ship packages from one port to another. The packages must be shipped within 'd' days.
The weights of the packages are given in an array 'of weights'. The packages are loaded on the conveyor belts every day in the same order as they appear in the array. The loaded weights must not exceed the maximum weight capacity of the ship.
Find out the least-weight capacity so that you can ship all the packages within 'd' days.
Example 1:
---------
Input Format: N = 5, weights[] = {5,4,5,2,3,4,5,6}, d = 5
Result: 9
Explanation: If the ship capacity is 9, the shipment will be done in the following manner:
Day         Weights            Total
1        -       5, 4          -        9
2        -       5, 2          -        7
3        -       3, 4          -        7
4        -       5              -        5
5        -       6              -        6
So, the least capacity should be 9.

Example 2:
----------
Input Format: N = 10, weights[] = {1,2,3,4,5,6,7,8,9,10}, d = 1
Result: 55
Explanation: We have to ship all the goods in a single day. So, the weight capacity should be the summation of all the weights i.e. 55.

"""


def find_days(packages, amount):
    curr = 0
    day = 1
    for pkg in packages:
        if curr + pkg > amount:
            curr = pkg
            day += 1
        else:
            curr += pkg
    return day


def capacity_to_ship_packages_with_d_days(packages, days):
    # Time complexity:
    max_weight = max(packages)
    sum_of_pack = sum(packages)

    low = max_weight
    high = sum_of_pack

    while low <= high:
        mid = (low + high) // 2

        if find_days(packages, mid) <= days:
            high = mid - 1
        else:
            low = mid + 1

    return low


if __name__ == '__main__':
    ex_1, ex_2 = ([5, 4, 5, 2, 3, 4, 5, 6], 5), ([
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)
    print(capacity_to_ship_packages_with_d_days(ex_1[0], ex_1[1]))
    print(capacity_to_ship_packages_with_d_days(ex_2[0], ex_2[1]))
