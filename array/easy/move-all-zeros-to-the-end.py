"""
1 ,0 ,2 ,3 ,0 ,4 ,0 ,1


Two pointer approach:
--------------------
start with two pointer:
first -> that will keep track of the zero position
second-> that will find the next non zero element position
    swap if first == 0 and second!= 0
    move first+=1, reset second to first
    if first!=0: move both first and second to next index
    if first== 0, move second to find the next non zero index
    repeat
Time complexity: O(n), Space complexity: O(1)
"""


def move_all_zeros_to_the_end(nums):
    n = len(nums)
    first = second = 0

    while first < n and second < n:
        if nums[first] == 0:
            if nums[second] != 0:
                nums[first], nums[second] = nums[second], nums[first]
                first += 1
                second = first
            else:
                second += 1
        else:
            first += 1
            second = first


"""    
[RECOMMENDED]
insert non zero  then zero with a count var:
---------------------
keep track of the non zero elem count with insert_pos var
and keep inserting non zero element at the beginning
When all non zero element has been finished, insert zero with the insert_pos count

Time complexity: O(n), Space complexity: O(1)
"""


def move_all_zeros_to_the_end_alter(nums):
    insert_pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[insert_pos] = nums[i]
            insert_pos += 1

    while insert_pos < len(nums):
        nums[insert_pos] = 0
        insert_pos += 1


if __name__ == '__main__':
    nums1, nums2, nums3, nums4 = [1, 0, 2, 3, 0, 4, 0, 1], [
        1, 2, 0, 1, 0, 4, 0], [0, 1, 0, 3, 12],  [0]
    func = move_all_zeros_to_the_end_alter
    func(nums1)
    print(nums1)
    func(nums2)
    print(nums2)
    func(nums3)
    print(nums3)
    func(nums4)
    print(nums4)
