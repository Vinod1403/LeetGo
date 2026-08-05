from collections import Counter

class Solution:
    def frequencySort(self, nums):

        count = Counter(nums)

        nums.sort(key=lambda x: (count[x], -x))

        return nums