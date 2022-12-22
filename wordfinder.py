"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """Finding random word from file
    >>> serial = WordFinder("words.txt")

    >>> serial.random() in open("words.txt").read()
    True
    """
    
    def __init__(self, path):
        """read file and return # read"""
        txt_file = open(path)
        self.words =self.parse(txt_file)
        print(f"{len(self.words)} words read")

    def parse(self, txt_file):
        """Remove spaces at the beginning and at the end of the string"""
        return [word.strip() for word in txt_file]
    def random(self):
        """return random"""
        return random.choice(self.words)
class SpecialWordFinder(WordFinder):
    """wordfinder ignore blank line and comment
    >>> serial = WordFinder("test.txt")

    >>> serial.random() in open("test.txt").read()
    True
    """
    def parse(self, txt_file):
        """remove newline and check if not start with #"""
        return [word.strip() for word in txt_file if word.strip() and not word.startswith("#")]

