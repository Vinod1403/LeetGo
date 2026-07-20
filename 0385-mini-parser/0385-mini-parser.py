class Solution:
    def deserialize(self, s):

        # Single integer
        if s[0] != '[':
            return NestedInteger(int(s))

        stack = []
        num = ""
        negative = False

        for ch in s:

            if ch == '[':
                stack.append(NestedInteger())

            elif ch == '-':
                negative = True

            elif ch.isdigit():
                num += ch

            elif ch == ',' or ch == ']':

                if num:
                    value = int(num)
                    if negative:
                        value = -value

                    stack[-1].add(NestedInteger(value))

                    num = ""
                    negative = False

                if ch == ']' and len(stack) > 1:
                    ni = stack.pop()
                    stack[-1].add(ni)

        return stack[-1]