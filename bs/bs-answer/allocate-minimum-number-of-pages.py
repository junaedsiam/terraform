"""
Problem description: 
---------
Given an array 'arr of integer numbers, 'ar[i]' represents the number of pages in the 'i-th' book. There are a 'm' number of students, and the task is to allocate all the books to the students.
Allocate books in such a way that:

Each student gets at least one book.
Each book should be allocated to only one student.
Book allocation should be in a contiguous manner.
You have to allocate the book to 'm' students such that the maximum number of pages assigned to a student is minimum. If the allocation of books is not possible. return -1
Example 1:
Input Format: n = 4, m = 2, arr[] = {12, 34, 67, 90}
Result: 113
Explanation: The allocation of books will be 12, 34, 67 | 90. One student will get the first 3 books and the other will get the last one.

Example 2:
Input Format: n = 5, m = 4, arr[] = {25, 46, 28, 49, 24}
Result: 71
Explanation: The allocation of books will be 25, 46 | 28 | 49 | 24.
"""


def count_students(nums, pages):
    n = len(nums)
    students = 1
    page_per_student = 0
    for i in range(n):
        if page_per_student+nums[i] <= pages:
            page_per_student += nums[i]
        else:
            page_per_student = nums[i]
            students += 1
    return students


def allocate_minimum_number_of_pages(nums, k):
    # Time complexity: O(n * log (m))
    low = max(nums)
    high = sum(nums)
    while low <= high:
        mid = (low + high) // 2
        if count_students(nums, mid) > k:
            low = mid + 1
        else:
            high = mid - 1
    return low


if __name__ == '__main__':
    ex_1, ex_2 = ([12, 34, 67, 90], 2), ([25, 46, 28, 49, 24], 4)
    print(allocate_minimum_number_of_pages(ex_1[0], ex_1[1]))
    print(allocate_minimum_number_of_pages(ex_2[0], ex_2[1]))
