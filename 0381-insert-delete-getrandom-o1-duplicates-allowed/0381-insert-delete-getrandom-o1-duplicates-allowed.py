from collections import defaultdict
import random

class RandomizedCollection:

    def __init__(self):
        self.nums = []
        self.pos = defaultdict(set)

    def insert(self, val):

        self.pos[val].add(len(self.nums))
        self.nums.append(val)

        return len(self.pos[val]) == 1

    def remove(self, val):

        if not self.pos[val]:
            return False

        removeIndex = self.pos[val].pop()
        lastVal = self.nums[-1]

        self.nums[removeIndex] = lastVal

        self.pos[lastVal].add(removeIndex)
        self.pos[lastVal].discard(len(self.nums) - 1)

        self.nums.pop()

        return True

    def getRandom(self):

        return random.choice(self.nums)