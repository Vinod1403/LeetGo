class Solution:
    def sumOfBeauties(self, nums):

        n = len(nums)

        prefixMax = [0] * n
        suffixMin = [0] * n

        prefixMax[0] = nums[0]
        for i in range(1, n):
            prefixMax[i] = max(prefixMax[i - 1], nums[i])

        suffixMin[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffixMin[i] = min(suffixMin[i + 1], nums[i])

        beauty = 0

        for i in range(1, n - 1):

            if prefixMax[i - 1] < nums[i] < suffixMin[i + 1]:
                beauty += 2

            elif nums[i - 1] < nums[i] < nums[i + 1]:
                beauty += 1

        return beauty