class Solution:
    def removeOccurrences(self, s, part):

        stack = []

        m = len(part)

        for ch in s:

            stack.append(ch)

            if len(stack) >= m:

                if "".join(stack[-m:]) == part:
                    for _ in range(m):
                        stack.pop()

        return "".join(stack)