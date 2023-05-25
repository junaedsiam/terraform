def partition(nums, low, high):
    # Picking the lowest value as pivot
    pivot = nums[low]
    # setting two pointers in the array. i for left-> right, j for right-> left
    i = low
    j = high

    while i < j:
        # if i value less than equal pivot. then its in correct position, move on right
        while nums[i] <= pivot and i < high:
            i += 1
        # If j value is greater than pivot, j value is in correct position. Move on left
        while nums[j] > pivot and j > low:
            j -= 1
        # In here we found i value that is greater than pivot, and j value which is less than pivot
        # We swap the position. Send the smalle value to small index, and large value to large index
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
        # Continue the loop until i is greater than equal j
    # Finally we found the partition index to put pivot in its correct place. Swap j index with low
    nums[j], nums[low] = nums[low], nums[j]
    # And return the partition index
    return j


def quick_sort(nums, low, high):
    if low < high:
        # First find partition index. Partition index is an index where the value is in correct position
        # So now we have to sort the left and right side of partition index
        pi = partition(nums, low, high)
        quick_sort(nums, low, pi - 1)
        quick_sort(nums, pi + 1, high)


if __name__ == '__main__':
    nums1, nums2 = [5, 3, 1, 2, 7, 16, 2], [3, 5, 1, 2, 7, 8]
    quick_sort(nums1, 0, len(nums1) - 1)
    print(nums1)
    quick_sort(nums2, 0, len(nums2) - 1)
    print(nums2)
