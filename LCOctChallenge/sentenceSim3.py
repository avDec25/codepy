class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        smaller = sentence1.split(' ')
        larger = sentence2.split(' ')
        if len(smaller) > len(larger):
            smaller, larger = larger, smaller

        l = 0
        while l < len(smaller) and smaller[l] == larger[l]:
            l += 1

        r1, r2 = len(smaller) - 1, len(larger) - 1
        while r1 >= 0 and r2 >= 0 and smaller[r1] == larger[r2]:
            r1 -= 1
            r2 -= 1

        return l > r1


sentence1 = "DN PD"
sentence2 = "D"
print(Solution().areSentencesSimilar(sentence1, sentence2) == False)
print("===================================")

sentence1 = "IfYgEidlr a QG kUqlcd J"
sentence2 = "IfYgEidlr xFi a B QG kUqlcd J HVbknBM ngNyvJo efrpY"
print(Solution().areSentencesSimilar(sentence1, sentence2) == False)
print("===================================")

sentence1 = "xD iP tqchblXgqvNVdi"
sentence2 = "FmtdCzv Gp YZf UYJ xD iP tqchblXgqvNVdi"
print(Solution().areSentencesSimilar(sentence1, sentence2) == True)
print("===================================")

sentence1 = "My name is Haley"
sentence2 = "My Haley"
print(Solution().areSentencesSimilar(sentence1, sentence2) == True)
print("===================================")

sentence1 = "Hello Jane"
sentence2 = "Hello my name is Jane"
print(Solution().areSentencesSimilar(sentence1, sentence2) == True)
print("===================================")

sentence1 = "eTUny i b R UFKQJ EZx JBJ Q xXz"
sentence2 = "eTUny i R EZx JBJ xXz"
print(Solution().areSentencesSimilar(sentence1, sentence2) == False)
print("===================================")

sentence1 = "of"
sentence2 = "A lot of words"
print(Solution().areSentencesSimilar(sentence1, sentence2) == False)
print("===================================")

sentence1 = "Frog cool"
sentence2 = "Frogs are cool"
print(Solution().areSentencesSimilar(sentence1, sentence2) == False)
print("===================================")

sentence1 = "Eating right now"
sentence2 = "Eating"
print(Solution().areSentencesSimilar(sentence1, sentence2) == True)
print("===================================")

sentence1 = "gozaimasu"
sentence2 = "Aarigato gozaimasu"
print(Solution().areSentencesSimilar(sentence1, sentence2) == True)
print("===================================")
