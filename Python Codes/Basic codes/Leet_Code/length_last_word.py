class Solution:
    def lengthOfLastWord(self, word: str) -> int:
        word_pieces = word.split()
        return len(word_pieces[-1])


print(Solution().lengthOfLastWord("   fly me   to   the moon  "))
