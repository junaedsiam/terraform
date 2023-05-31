# To search in a sorted 2d matrix, we can perform binary search.
# Now there are two ways to perform the search

# --------------
# Number 1: We will individually find the row which possible contains the value
# by searching first. And in second step, we will search only row to find if the values exists or not
# This Does the tric

def binary_search(nums, n, target):
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return True
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return True if nums[low] == target else False


def search_in_a_sorted_matrix(mat, target):
    # Time complexity: O(log(m + n)), Space complexity: O(1)

    n = len(mat)
    m = len(mat[0])

    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        # target less than zero index value
        if mat[mid][0] > target:
            high = mid - 1
        # target is greater than last index value
        elif mat[mid][m - 1] < target:
            low = mid + 1
        # Target is in between
        else:
            return binary_search(mat[mid], m, target)


# Number 2: Instead of searching 2 times ones searching the row, then searching element in the row.
# We can search in one go. Idea is, we can think the whole 2d array as 1d array containing (m * n) elements
# Low will be 0, high will be (m * n) - 1
def search_in_a_sorted_matrix_alter(mat, target):
    # Time complexity: O(log(m + n)), Space complexity: O(1)
    n = len(mat)
    m = len(mat[0])

    low = 0
    high = (n * m) - 1

    while low <= high:
        mid = (low + high) // 2
        val = mat[mid // m][mid % m]
        if val == target:
            return True
        elif val > target:
            high = mid - 1
        else:
            low = mid + 1

    return False


if __name__ == '__main__':
    func = search_in_a_sorted_matrix_alter
    mat1, mat2 = [[1, 3, 5, 7],
                  [10, 11, 16, 20],
                  [23, 30, 34, 60]], [[1, 3, 5, 7],
                                      [10, 11, 16, 20],
                                      [23, 30, 34, 60]]
    target1, target2 = 3, 13

    print(func(mat1, target1))
    print(func(mat2, target2))
