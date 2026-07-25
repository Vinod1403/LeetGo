from collections import Counter

class Solution:
    def minimumRounds(self, tasks):

        count = Counter(tasks)
        rounds = 0

        for freq in count.values():

            if freq == 1:
                return -1

            if freq % 3 == 0:
                rounds += freq // 3
            else:
                rounds += freq // 3 + 1

        return rounds