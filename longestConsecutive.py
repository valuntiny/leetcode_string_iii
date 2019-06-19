'''
Quest:
    Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
    Your algorithm should run in O(n) complexity.

    Example:
    Input: [100, 4, 200, 1, 3, 2]
    Output: 4

    Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Solution:
    - here we can use set() function, elements in set doesnt have order, so can not access through index.
        but good thing is the "in" judge in set take short time
'''


class Solution:
    def longestConsecutive(self, nums):
        res = 0
        nums = set(nums)
        for x in nums:
            # judge if it's a start of sequence
            if x-1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                res = max(res, y - x)

        return res

test = Solution()
x = [100, 4, 200, 1, 3, 2, 5, 7]
print(test.longestConsecutive(x))