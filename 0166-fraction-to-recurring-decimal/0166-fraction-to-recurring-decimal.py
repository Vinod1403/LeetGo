class Solution:
    def fractionToDecimal(self, numerator, denominator):

        if numerator == 0:
            return "0"

        ans = []

        # Sign
        if (numerator < 0) != (denominator < 0):
            ans.append("-")

        numerator = abs(numerator)
        denominator = abs(denominator)

        # Integer part
        ans.append(str(numerator // denominator))

        remainder = numerator % denominator

        if remainder == 0:
            return "".join(ans)

        ans.append(".")

        seen = {}

        while remainder:

            if remainder in seen:
                index = seen[remainder]
                ans.insert(index, "(")
                ans.append(")")
                break

            seen[remainder] = len(ans)

            remainder *= 10
            ans.append(str(remainder // denominator))
            remainder %= denominator

        return "".join(ans)