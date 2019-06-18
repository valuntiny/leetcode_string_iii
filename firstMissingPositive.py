'''
Quest:
    Given an unsorted integer array, find the smallest missing positive integer.

    Example 1:
    Input: [1,2,0]
    Output: 3

    Example 2:
    Input: [3,4,-1,1]
    Output: 2

    Example 3:
    Input: [7,8,9,11,12]
    Output: 1

    Note:
    Your algorithm should run in O(n) time and uses constant extra space.

Solution:
    use hash table, but instead of creating one, we can use the index of the array as the hash [0, 1, 2, 3, ..., n]
    if the length of array is l, then the firstMissingPositive must within [1,l+1] range: [0, 1, ..., l]
'''


class Solution:
    def firstMissingPositive(self, nums):
        nums.append(0)
        l = len(nums)

        for i in range(l):
            if nums[i] < 1 or nums[i] >= l:
                nums[i] = 0

        for i in range(l):
            nums[nums[i] % l] += l

        for i in range(1, l):
            if nums[i] // l == 0:
                return i

        return l

test = Solution()
x = [1,2,3,4,5]
print(test.firstMissingPositive(x))