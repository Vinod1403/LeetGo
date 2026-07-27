class Solution:
    def decodeCiphertext(self, encodedText, rows):

        if rows == 1:
            return encodedText.rstrip()

        n = len(encodedText)
        cols = n // rows

        ans = []

        for c in range(cols):

            i = 0
            j = c

            while i < rows and j < cols:
                ans.append(encodedText[i * cols + j])
                i += 1
                j += 1

        return "".join(ans).rstrip()