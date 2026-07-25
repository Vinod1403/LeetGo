class Solution:
    def minSwaps(self, nums):

        ones = sum(nums)

        if ones <= 1:
            return 0

        nums = nums + nums

        zeros = 0

        for i in range(ones):
            if nums[i] == 0:
                zeros += 1

        ans = zeros

        left = 0

        for right in range(ones, len(nums)):

            if nums[right] == 0:
                zeros += 1

            if nums[left] == 0:
                zeros -= 1

            left += 1

            if left >= len(nums) // 2:
                break

            ans = min(ans, zeros)

        return ans