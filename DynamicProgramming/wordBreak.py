class Solution:

    def checkPrefix(self, text):
        if not text: return True

        for i in range(1, len(text) + 1):
            prefix = text[:i]
            if prefix in self.dic and self.checkPrefix(text[i:]):
                return True

        return False

    def wordBreak(self, n, text, dictionary):
        self.dic = dictionary
        return self.checkPrefix(text)


if __name__ == '__main__':
    dictionary = {"i", "like", "sam", "sung", "samsung", "mobile", "ice",
                  "cream", "icecream", "man", "go", "mango"}
    n = len(dictionary)
    text = "ilikesamsung"
    print(Solution().wordBreak(n, text, dictionary))
