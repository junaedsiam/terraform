"""
Problem Statement: This problem has 3 variations. They are stated below:

Variation 1: Given row number r and column number c. Print the element at position (r, c) in Pascal's triangle.

Variation 2: Given the row number n. Print the n-th row of Pascal's triangle.

Variation 3: Given the number of rows n. Print the first n rows of Pascal's triangle.
"""

# Helper


def nCr(n, r):
    # Formula of nCr is nCr = n! / (r! * (n-r)!)
    # Looks like we have to n!, r! and then (n-r)! to find out the value.
    # We can optimize this calculation by the following observation.
    # Assume, given r = 7, c = 4.
    # Now, n = r-1 = 7-1 = 6 and r = c-1 = 4-1 = 3
    # Let’s calculate 6C3 = 6! / (3! *(6-3)!) = (6*5*4*3*2*1) / ((3*2*1)*(3*2*1))
    # This will boil down to (6*5*4) / (3*2*1)
    # So, nCr = (n*(n-1)*(n-2)*.....*(n-r+1)) / (r*(r-1)*(r-2)*....1)

    res = 1
    for i in range(r):
        res *= (n - i)
        res //= i + 1
    return res


def get_element_from_pascal_triangle(row, col):
    # VARIANT: 1
    # if (row, col) is given and you have to find out the element in that coordinate
    # To achieve that, we can do nCr to get the element in that position
    # In our case n = row - 1, r = col - 1
    # Time complexity: O(row), # Space complexity: O(1)
    return nCr(row - 1, col - 1)


def get_row(row):
    # VARIANT: 2
    # get the entire row
    # Observation: A row has same number of elements (columns). 6th row has 6 elements
    # BRUTE FORCE: in a brute force way we can follow above approach
    # to get all the elements in a given row. In that case row will be fixed, but
    # column will go from 0 to row -1
    # Time complexity: O ( row * col ), Space complexity: O(col)
    # OPTIMAL APPROACH: Formula for each element, element = prevElement * (row - col) / col
    # Time complexity: O(row), Space complexity: O(1)
    ls = [1]
    ans = 1
    for i in range(1, row):
        ans *= (row - i)
        ans //= i
        ls.append(ans)
    return ls


def get_triangle_till_nth(n):
    # Variant 3
    # Get the full triangle
    # Time complexity: O(n ^ 2), Space complexity: O(1)

    triangle = []
    for i in range(n):
        triangle.append(get_row(i + 1))
    return triangle


if __name__ == '__main__':
    print(get_element_from_pascal_triangle(7, 3))
    print(get_row(7))
    print(get_triangle_till_nth(7))
