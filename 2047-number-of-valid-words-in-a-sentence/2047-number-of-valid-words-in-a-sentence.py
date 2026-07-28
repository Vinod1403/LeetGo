class Solution:
    def countValidWords(self, sentence):

        words = sentence.split()
        ans = 0

        for word in words:

            hyphen = 0
            valid = True

            for i in range(len(word)):

                ch = word[i]

                if ch.isdigit():
                    valid = False
                    break

                elif ch == '-':
                    hyphen += 1

                    if (hyphen > 1 or
                        i == 0 or
                        i == len(word) - 1 or
                        not word[i - 1].islower() or
                        not word[i + 1].islower()):
                        valid = False
                        break

                elif ch in "!.,":

                    if i != len(word) - 1:
                        valid = False
                        break

                elif not ch.islower():
                    valid = False
                    break

            if valid:
                ans += 1

        return ans