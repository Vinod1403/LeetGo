class Solution:
    def palindromePairs(self, words):

        def isPalindrome(s):
            return s == s[::-1]

        wordIndex = {word: i for i, word in enumerate(words)}
        ans = []

        for i, word in enumerate(words):

            for j in range(len(word) + 1):

                left = word[:j]
                right = word[j:]

                # Left is palindrome
                if isPalindrome(left):
                    rev = right[::-1]
                    if rev in wordIndex and wordIndex[rev] != i:
                        ans.append([wordIndex[rev], i])

                # Right is palindrome
                # j != len(word) avoids duplicate pairs
                if j != len(word) and isPalindrome(right):
                    rev = left[::-1]
                    if rev in wordIndex and wordIndex[rev] != i:
                        ans.append([i, wordIndex[rev]])

        return ans