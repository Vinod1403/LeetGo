from collections import defaultdict

class Solution:
    def countKDifference(self, nums, k):

        count = defaultdict(int)
        ans = 0

        for num in nums:

            ans += count[num - k]
            ans += count[num + k]

            count[num] += 1

        return ans