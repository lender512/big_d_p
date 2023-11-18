from __future__ import annotations
from collections import OrderedDict
from fuzzywuzzy import fuzz
import nltk
from src.interfaces.Module import Module

class UpperCase(Module):
    def execute(self, input: str):
        self.result = input.upper()

class LowerCase(Module):
    def execute(self, input: str):
        self.result = input.lower()

class FuzzyClean(Module):
    threshold = 0.9

    def __init__(self, next: Module = None, threshold: float = 0.9):
        super().__init__(next)
        self.threshold = threshold


    def execute(self, input: str):
        filtered_words = []
        splited_words = input.split()
        for i in range(len(splited_words)-1):
            score = fuzz.ratio(splited_words[i], splited_words[i+1])
            filtered_words.append(splited_words[i]) if score < self.threshold*100 else None
        self.result = " ".join(filtered_words)


class RemoveStopWords(Module):
    nltk.download('stopwords')
    stopword_es = nltk.corpus.stopwords.words('spanish')

    def execute(self, input: str):
        filtered_words = []
        splited_words = input.split()
        for word in splited_words:
            if word not in self.stopword_es:
                filtered_words.append(word)
        self.result = " ".join(filtered_words)

class RemoveNonExistingWords(Module):
    nltk.download('cess_esp')
    stopword_es = set(nltk.corpus.cess_esp.words())

    def execute(self, input: str):
        filtered_words = []
        splited_words = input.split()
        for word in splited_words:
            if word in self.stopword_es:
                filtered_words.append(word)
        self.result = " ".join(filtered_words)


