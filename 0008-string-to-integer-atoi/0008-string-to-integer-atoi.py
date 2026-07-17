class Solution:
    def myAtoi(self, s):

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        i = 0
        n = len(s)

        # Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # Check sign
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        ans = 0

        # Read digits
        while i < n and s[i].isdigit():

            digit = ord(s[i]) - ord('0')

            # Check overflow
            if ans > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            ans = ans * 10 + digit
            i += 1

        return sign * ans