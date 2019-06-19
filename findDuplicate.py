'''
Quest:
    Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
    prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

    Example 1:
    Input: [1,3,4,2,2]
    Output: 2

    Example 2:
    Input: [3,1,3,4,2]
    Output: 3

    Note:
    You must not modify the array (assume the array is read only).
    You must use only constant, O(1) extra space.
    Your runtime complexity should be less than O(n2).
    There is only one duplicate number in the array, but it could be repeated more than once.

Solution:
    - (sum(x) - sum(set(x))) / (len(x) - len(set(x))) ... haha jk
    - think of it as a linked list, then if there is repreat, it'll end up in a loop,
        and the start point is the repeat number,
        use two pointer: slow (one step each time) and fast (two step each time)
        they will meet in the loop, but not necessarily meet up at start point
    - Assume the distance from head to the start of the loop is x1
        the distance from the start of the loop to the point fast and slow meet is x2
        the distance from the point fast and slow meet to the start of the loop is x3

        What is the distance fast moved? 2. What is the distance slow moved? 3. And their relationship?
        1: x1 + x2 + x3 + x2
        2: x1 + x2
        3: x1 + x2 + x3 + x2 = 2 (x1 + x2)
        Thus x1 = x3, that's the reason we reset fast to be 0.
'''


class Solution:
    def findDuplicate(self, nums):
        if not nums:
            return None

        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow, fast = nums[slow], nums[nums[fast]]

        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

test = Solution()
x = [3,1,3,4,2]
print(test.findDuplicate(x))