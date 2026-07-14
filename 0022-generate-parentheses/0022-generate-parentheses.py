class Solution:
    def generateParenthesis(self, n):

        ans = []

        def backtrack(curr, openCount, closeCount):

            if len(curr) == 2 * n:
                ans.append(curr)
                return

            if openCount < n:
                backtrack(curr + "(", openCount + 1, closeCount)

            if closeCount < openCount:
                backtrack(curr + ")", openCount, closeCount + 1)

        backtrack("", 0, 0)
        return ans