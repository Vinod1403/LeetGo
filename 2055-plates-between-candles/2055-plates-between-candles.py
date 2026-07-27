from bisect import bisect_left, bisect_right

class Solution:
    def platesBetweenCandles(self, s, queries):

        prefix = [0] * (len(s) + 1)
        candles = []

        for i in range(len(s)):
            prefix[i + 1] = prefix[i]

            if s[i] == '*':
                prefix[i + 1] += 1
            else:
                candles.append(i)

        ans = []

        for left, right in queries:

            l = bisect_left(candles, left)
            r = bisect_right(candles, right) - 1

            if l >= len(candles) or r < 0 or l >= r:
                ans.append(0)
            else:
                leftCandle = candles[l]
                rightCandle = candles[r]

                ans.append(prefix[rightCandle] - prefix[leftCandle])

        return ans