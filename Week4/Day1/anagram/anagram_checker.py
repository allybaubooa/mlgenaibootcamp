import os

class AnagramChecker:
    def __init__(self, filename= "sowpods.txt"):
        self.words: str = set()

        with open(filename,"r", encoding="utf-8") as s:
            for lines in s:
                word = lines.strip().upper()
                if lines:
                    self.words.add(word)

    def is_valid_word(self, word: str):
        a = word.strip().upper()
        return a in self.words
    
    def is_anagram(self, word1: str, word2: str):
        w1 = word1.strip().upper()
        w2 = word2.strip().upper()
        
        if w1 == w2:
            return False
        
        if len(w1) != len(w2):
            return False
        
        return sorted(w1) == sorted(w2)
    
    def get_anagrams(self, word: str):
        a = word.strip().upper()
        anagrams = []
        
        for dict in self.words:
            if self.is_anagram(a, dict):
                anagrams.append(dict.lower())

        return anagrams