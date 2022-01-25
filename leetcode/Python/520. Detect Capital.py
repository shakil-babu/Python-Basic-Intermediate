class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        copy = word[:]
        if copy == word.upper() :
            return True
        if copy == word.lower() :
            return True
        if copy == word.capitalize():
            return True
        else :
            return False