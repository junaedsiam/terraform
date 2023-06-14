"""
Majority Elements(>N/3 times) | Find the elements that appears more than N/3 times in the array
Problem Statement: Given an array of N integers. Find the elements that appear more than N/3 times in the array. If no such element exists, return an empty vector.
Example 1:
Input Format: N = 5, array[] = {1,2,2,3,2}
Result: 2
Explanation: Here we can see that the Count(1) = 1, Count(2) = 3 and Count(3) = 1.Therefore, the count of 2 is greater than N/3 times. Hence, 2 is the answer.

Example 2:
Input Format:  N = 6, array[] = {11,33,33,11,33,11}
Result: 11 33
Explanation: Here we can see that the Count(11) = 3 and Count(33) = 3. Therefore, the count of both 11 and 33 is greater than N/3 times. Hence, 11 and 33 is the answer.

"""
# Observation: At most 2 element can appear more than n /3 times in a given array.
# Brute force: Just take each element, and loop through the whole array to find out if it occurs more than n / 3
# Time complexity: O(n ^ 2), Space complexity: O(1)
# Hashing: We will keep track of the count of  previously visited elements, and then finally we will check the hashlist to find
# If any elements have been appeared more than n /3
# Time complexity: O(2n) , Space complexity: O(n)


def n_by_3_majority_element(nums):
    # Optimal approach: A modified version of moore's voting algorithm
    # Time complexity: O(n), Space complexity: O(1)
    count1, count2 = 0, 0
    element1, element2 = float('-inf'), float('-inf')
    n = len(nums)
    for i in range(n):
        if count1 == 0 and nums[i] != element2:
            count1 = 1
            element1 = nums[i]
        elif count2 == 0 and nums[i] != element1:
            count2 = 1
            element2 = nums[i]
        elif nums[i] == element1:
            count1 += 1
        elif nums[i] == element2:
            count2 += 1
        else:
            count1 -= 1
            count2 -= 1
    # Verification loop
    count1, count2 = 0, 0
    for i in range(n):
        if nums[i] == element1:
            count1 += 1
        elif nums[i] == element2:
            count2 += 1

    ls = []
    if count1 > n // 3:
        ls.append(element1)
    if count2 > n // 3:
        ls.append(element2)

    return ls


if __name__ == '__main__':
    nums1, nums2 = [1, 2, 2, 3, 2], [11, 33, 33, 11, 33, 11]
    print(n_by_3_majority_element(nums1))
    print(n_by_3_majority_element(nums2))
