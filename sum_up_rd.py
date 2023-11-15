from __future__ import annotations
from collections import OrderedDict
from fuzzywuzzy import fuzz
import nltk
import os

class Module(object):
    name: str = ""
    next: Module = None
    result: any = None

    def __init__(self, next: Module = None):
        self.name = self.__class__.__name__
        self.next = next

    def execute(self, *args):
        pass

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

class Sequential(object):
    startModule = None
    input = None

    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], OrderedDict):
            for module in args[0]:
                self.add(module)
        else:
            for module in args:
                self.add(module)

    def add(self, module: Module):
        if self.startModule is None:
            self.startModule = module
        else:
            currentModule = self.startModule
            while currentModule.next is not None:
                currentModule = currentModule.next
            currentModule.next = module

    def set_input(self, input):
        self.input = input

    def forward(self):
        currentModule = self.startModule
        while currentModule is not None:
            print(f"Executing {currentModule.name}")
            currentModule.execute(self.input)
            self.input = currentModule.result
            currentModule = currentModule.next
        return self.input

if __name__ == "__main__":
    #read file
    input = ""
    with open("trans/radio_imperial.txt", "r") as f:
        input = f.read()

    seq = Sequential(
        LowerCase(),
        FuzzyClean(threshold=0.9),
        RemoveStopWords(),
        RemoveNonExistingWords()
    )
    print(len(input))
    seq.set_input(input)
    result = seq.forward()
    print(len(result))