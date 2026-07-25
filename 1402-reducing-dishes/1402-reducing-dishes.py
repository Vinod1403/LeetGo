class Solution:
    def maxSatisfaction(self, satisfaction):

        satisfaction.sort()

        suffixSum = 0
        answer = 0

        for i in range(len(satisfaction) - 1, -1, -1):

            suffixSum += satisfaction[i]

            if suffixSum > 0:
                answer += suffixSum
            else:
                break

        return answer