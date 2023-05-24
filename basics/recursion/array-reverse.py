def reverse_array(nums, start, end):
    if start < end:
        nums[start], nums[end] = nums[end], nums[start]
        reverse_array(nums, start+1, end - 1)


if __name__ == '__main__':
    num1 = [5, 4, 3, 2, 1]
    num2 = [1, 2, 3, 4, 5]

    reverse_array(num1, 0, len(num1) - 1)
    print(num1)
    reverse_array(num2, 0, len(num2) - 1)
    print(num2)
