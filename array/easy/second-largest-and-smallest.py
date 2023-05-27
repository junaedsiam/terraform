def second_largest_and_smallest(nums):
    n = len(nums)
    if n <= 1:
        return [-1, -1]
    lg, sm = (nums[0], nums[1]) if nums[0] > nums[1] else (nums[1], nums[0])
    sec_lg, sec_sm = sm, lg
    for i in range(2, n):
        # if current value is greater than largest
        if nums[i] > lg:
            lg = nums[i]
        # if current value is smaller than smallest
        elif nums[i] < sm:
            sm = nums[i]
        # if current value is less than largest, but greater than sec largest
        if nums[i] < lg and nums[i] > sec_lg:
            sec_lg = nums[i]
        # if current value is greater than smallest, but smaller than sec_smallest
        if nums[i] > sm and nums[i] < sec_sm:
            sec_sm = nums[i]
    return [sec_lg, sec_sm]


if __name__ == '__main__':
    num1, num2 = [1, 2, 4, 7, 7, 5], [1, 6, 5, 9, 8, 2, 3, 4, 7]
    print(second_largest_and_smallest(num1))
    print(second_largest_and_smallest(num2))
