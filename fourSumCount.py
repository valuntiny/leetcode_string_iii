'''
Quest:
    Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are
    such that A[i] + B[j] + C[k] + D[l] is zero.
    To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500.
    All integers are in the range of -2^28 to 2^28 - 1 and the result is guaranteed to be at most 231 - 1.

    Example:

    Input:
    A = [ 1, 2]
    B = [-2,-1]
    C = [-1, 2]
    D = [ 0, 2]

    Output:
    2

    Explanation:
    The two tuples are:
    1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
    2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

Solution:
    - recursion?
    - hashmap, since A + B + C + D = 0, then A + B = - C - D
        create a hashmap of A+B, and if A+B[-C-D] exist, then there it is
'''


class Solution:
    def fourSumCount(self, A, B, C, D):
        res = 0
        hashmap = {}

        for a in A:
            for b in B:
                if a+b in hashmap:
                    hashmap[a + b] += 1
                else:
                    hashmap[a + b] = 1

        for c in C:
            for d in D:
                if -c-d in hashmap:
                    res += hashmap[-c-d]

        return res

test = Solution()
A = [1, 2]
B = [-2, -1]
C = [-1, 2]
D = [0, 2]
print(test.fourSumCount(A, B, C, D))