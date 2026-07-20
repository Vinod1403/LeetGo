class Solution:
    def minimumAverageDifference(self, nums):

        n = len(nums)
        total = sum(nums)

        leftSum = 0
        minDiff = float("inf")
        ans = 0

        for i in range(n):

            leftSum += nums[i]

            leftAvg = leftSum // (i + 1)

            if i == n - 1:
                rightAvg = 0
            else:
                rightAvg = (total - leftSum) // (n - i - 1)

            diff = abs(leftAvg - rightAvg)

            if diff < minDiff:
                minDiff = diff
                ans = i

        return ans