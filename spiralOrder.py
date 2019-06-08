'''
Quest:
    Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

    Example 1:
    Input:
    [
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]
    ]
    Output: [1,2,3,6,9,8,7,4,5]

    Example 2:
    Input:
    [
      [1, 2, 3, 4],
      [5, 6, 7, 8],
      [9,10,11,12]
    ]
    Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Solution:
    - (i, j): can not loop between i and j because there'll be too many
    - there could be loop, but each loop shall loop within a whole border,
      then at the end , we decide what's left (nothing / vertical vector / horizontal vector)
'''


class Solution:
    def spiralOrder(self, matrix):
        res = []
        if not matrix or not matrix[0]:
            return res

        left, right, upper, lower = 0, len(matrix[0])-1, 0, len(matrix)-1
        while left < right and upper < lower:
            res.extend(matrix[upper][j] for j in range(left, right))
            res.extend(matrix[i][right] for i in range(upper, lower))
            res.extend(matrix[lower][j] for j in range(right, left, -1))
            res.extend(matrix[i][left] for i in range(lower, upper, -1))
            left, right, upper, lower = left+1, right-1, upper+1, lower-1

        # deal with the ending situation: horizontal vector
        if upper == lower:
            res.extend(matrix[lower][j] for j in range(left, right+1))
        # deal with the ending situation: vertical vector
        elif left == right:
            res.extend(matrix[i][left] for i in range(upper, lower+1))

        return res

test = Solution()
x = [[1,2],[3,4]]
print(test.spiralOrder(x))
