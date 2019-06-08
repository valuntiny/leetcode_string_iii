'''
Quest:
    Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal
    to the product of all the elements of nums except nums[i].

    Example:
    Input:  [1,2,3,4]
    Output: [24,12,8,6]

    Note: Please solve it without division and in O(n).

    Follow up:
    Could you solve it with constant space complexity?
    (The output array does not count as extra space for the purpose of space complexity analysis.)

Solution:
    - use two loop, first loop from left to right, doing the product gradually without itself
      [1, (0), (0)*(1), ..., (0)*(1)*...*(n-4), (0)*(1)*...*(n-3), (0)*(1)*...*(n-2)]
    - second one from right to left, doing product again without itself
      [*1, *(n-1), *(n-1)*(n-2)..., *(n-1)*...*(2), *(n-1)*...*(1)]
'''


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        p = 1
        res.append(p)
        n = len(nums)

        for i in range(1, n):
            p *= nums[i-1]
            res.append(p)

        p = 1
        for j in range(n-1, -1, -1):
            res[j] *= p
            p *= nums[j]

        return res