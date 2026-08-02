class Solution:
    def countTriples(self, n):

        squares = set()

        for i in range(1, n + 1):
            squares.add(i * i)

        ans = 0

        for a in range(1, n + 1):
            for b in range(1, n + 1):

                if a * a + b * b in squares:
                    ans += 1

        return ans