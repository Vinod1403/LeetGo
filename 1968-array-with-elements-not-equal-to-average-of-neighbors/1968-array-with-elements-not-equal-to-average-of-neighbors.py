class Solution:
    def rearrangeArray(self, nums):

        nums.sort()

        ans = []

        left = 0
        right = len(nums) - 1

        while left <= right:

            if left <= right:
                ans.append(nums[left])
                left += 1

            if left <= right:
                ans.append(nums[right])
                right -= 1

        return ans