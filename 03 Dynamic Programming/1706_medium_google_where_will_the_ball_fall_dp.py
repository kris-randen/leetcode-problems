"""
1706. Where Will the Ball Fall
Medium
2.9K
171
company
Google
company
Amazon
You have a 2-D grid of size m x n representing a box, and you have n balls. The box is open on the top and bottom sides.

Each cell in the box has a diagonal board spanning two corners of the cell that can redirect a ball to the right or to the left.

A board that redirects the ball to the right spans the top-left corner to the bottom-right corner and is represented in the grid as 1.
A board that redirects the ball to the left spans the top-right corner to the bottom-left corner and is represented in the grid as -1.
We drop one ball at the top of each column of the box. Each ball can get stuck in the box or fall out of the bottom. A ball gets stuck if it hits a "V" shaped pattern between two boards or if a board redirects the ball into either wall of the box.

Return an array answer of size n where answer[i] is the column that the ball falls out of at the bottom after dropping the ball from the ith column at the top, or -1 if the ball gets stuck in the box.



Example 1:



Input: grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
Output: [1,-1,-1,-1,-1]
Explanation: This example is shown in the photo.
Ball b0 is dropped at column 0 and falls out of the box at column 1.
Ball b1 is dropped at column 1 and will get stuck in the box between column 2 and 3 and row 1.
Ball b2 is dropped at column 2 and will get stuck on the box between column 2 and 3 and row 0.
Ball b3 is dropped at column 3 and will get stuck on the box between column 2 and 3 and row 0.
Ball b4 is dropped at column 4 and will get stuck on the box between column 2 and 3 and row 1.
Example 2:

Input: grid = [[-1]]
Output: [-1]
Explanation: The ball gets stuck against the left wall.
Example 3:

Input: grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
Output: [0,1,2,3,4,-1]
"""

from enum import Enum


class Direction(Enum):
    DOWN = 1
    RIGHT = 2
    LEFT = 3
    UP = -1



def direct(directions, angles):
    n = len(directions)
    new = [Direction.UP for _ in range(n)]
    for i in range(n):
        if angles[i] == 1:
            if i == n - 1:
                continue
            if directions[i] == Direction.DOWN:
                new[i + 1] = Direction.RIGHT
            elif directions[i] == Direction.RIGHT:
                new[i] = Direction.DOWN
            elif directions[i] == Direction.LEFT:
                new[i] = Direction.UP
        elif angles[i] == -1:
            if i == 0:
                continue
            if directions[i] == Direction.DOWN:
                new[i - 1] = Direction.LEFT
            elif directions[i] == Direction.LEFT:
                new[i] = Direction.DOWN
            elif directions[i] == Direction.RIGHT:
                new[i] = Direction.UP
    return new

def path(directions, matrix):
    vertical = directions
    for angles in matrix:
        horizontal = direct(vertical, angles)
        vertical = direct(horizontal, angles)
    return list(map(lambda x: 1 if x == Direction.DOWN else -1, vertical))

