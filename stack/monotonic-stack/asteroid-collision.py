"""
Problem description: 
---------
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
 

Constraints:

2 <= asteroids.length <= 104
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0
"""

from typing import List


def asteroid_collision(asteroids: List[int]) -> List[int]:
    # Time complexity: O(n)
    res = []
    for i in range(len(asteroids)):
        while len(res) and asteroids[i] < 0 and res[-1] > 0:
            # stack top equal to the -asteroid[i]
            if res[-1] == -asteroids[i]:
                res.pop()
                break
            # stack top is less than the -asteroid[i]
            if res[-1] < -asteroids[i]:
                res.pop()
                continue
            # stack top is greater than -asteroid[i]
            else:
                break
        else:
            # Some other condition
            res.append(asteroids[i])
    return res


if __name__ == '__main__':
    print(asteroid_collision([5, 10, -5]))
    print(asteroid_collision([8, -8]))
    print(asteroid_collision([10, 2, -5]))
