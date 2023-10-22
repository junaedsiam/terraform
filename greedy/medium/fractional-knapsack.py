"""
Problem description: 
---------
Given weights and values of N items, we need to put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
Note: Unlike 0/1 knapsack, you are allowed to break the item. 

Example 1:

Input:
N = 3, W = 50
values[] = {60,100,120}
weight[] = {10,20,30}
Output:
240.00
Explanation:Total maximum value of item
we can have is 240.00 from the given
capacity of sack. 
Example 2:

Input:
N = 2, W = 50
values[] = {60,100}
weight[] = {10,20}
Output:
160.00
Explanation:
Total maximum value of item
we can have is 160.00 from the given
capacity of sack.
 

Your Task :
Complete the function fractionalKnapsack() that receives maximum capacity , array of structure/class and size n and returns a double value representing the maximum value in knapsack.
Note: The details of structure/class is defined in the comments above the given function.


Expected Time Complexity : O(NlogN)
Expected Auxilliary Space: O(1)


Constraints:
1 <= N <= 105
1 <= W <= 105
"""


class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight


def fractional_knapsack(weight_cap, item_list):
    # Time complexity: O(n log n)
    curr_w = 0
    res = 0
    # Sort the items, in a descending order based on value / weight ratio
    item_list.sort(key=lambda x: x.value / x.weight, reverse=True)
    # Run a for loop to traverse through the item
    for item in item_list:
        # # if the weight of the item is less than or equal to remaining weight,
        # # add the item directy to the knapsack
        if curr_w + item.weight <= weight_cap:
            curr_w += item.weight
            res += item.value
        else:
            rem = (weight_cap - curr_w) / item.weight
            res += item.value * rem
            break
    # # else put only the remaining weight amount and add the value
    # return value
    return res


if __name__ == '__main__':
    print(fractional_knapsack(
        50, [Item(60, 10), Item(100, 20), Item(120, 30)]))
