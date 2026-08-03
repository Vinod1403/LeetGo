class Solution:
    def canChoose(self, groups, nums):

        i = 0
        j = 0

        while i < len(groups) and j < len(nums):

            group = groups[i]

            if nums[j:j + len(group)] == group:
                j += len(group)
                i += 1
            else:
                j += 1

        return i == len(groups)