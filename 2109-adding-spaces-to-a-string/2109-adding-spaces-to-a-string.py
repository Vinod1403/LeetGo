class Solution:
    def addSpaces(self, s, spaces):

        ans = []
        j = 0

        for i in range(len(s)):

            if j < len(spaces) and i == spaces[j]:
                ans.append(" ")
                j += 1

            ans.append(s[i])

        return "".join(ans)