# Given an Array A, find the minimum amplitude you can get after changing up to 3 elements. Amplitude is the range of the array (basically difference between largest and smallest element).

# Example 1:

# Input: [-1, 3, -1, 8, 5 4]
# Output: 2
# Explanation: we can change -1, -1, 8 to 3, 4 or 5

# Example 2:

# Input: [10, 10, 3, 4, 10]
# Output: 0
# Explanation: change 3 and 4 to 10

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        return min(nums[-1] - nums[3], nums[-2] - nums[2], nums[-3] - nums[1], nums[-4] - nums[0])