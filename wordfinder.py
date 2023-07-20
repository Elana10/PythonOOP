"""Word Finder: finds random words from a dictionary."""
from random import randint

class WordFinder:
    def __init__(self,file):
        self.file_path = file
        self.word_dict = self.save_words()
        self.word_c = self.word_count()
        print(f"{self.word_c} words read")
    
    def __repr__(self):
        return f"{self.word_c} words read"

    def save_words(self):
        words = open(self.file_path, 'r')
        new_dict = {}
        for line in words:
            if line.strip() in new_dict:
                new_dict[line.strip()] += 1
            else:
                new_dict[line.strip()] = 1
        words.close()
        return new_dict
    # https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-12.php

    def word_count(self):
        return len(self.word_dict)
    
    def random(self):
        dk = list(self.word_dict.keys())
        return dk[randint(0,self.word_c)]
    
        
class SpecialWordFinder(WordFinder):
    def __init__(self, file_path):
        super().__init__(file_path)
        self.word_dict = self.save_words()
        self.word_c = super().word_count()
        print(f"{self.word_c} words read")
    
    def __repr__(self):
        answer = super().__repr__()
        return answer
    
    def save_words(self):
        words = open(self.file_path, 'r')
        new_dict = {}
        for line in words:
            if line.strip() != '' or line.strip() != '#':
                if line.strip() in new_dict:
                    new_dict[line.strip()] += 1
                else:
                    new_dict[line.strip()] = 1
        words.close()
        return new_dict
