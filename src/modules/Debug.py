from __future__ import annotations
from collections import OrderedDict
from fuzzywuzzy import fuzz
import nltk
from src.interfaces.Module import Module
from sklearn.feature_extraction.text import TfidfVectorizer 
import numpy as np

class SaveInputModule(Module):
    path = None
    def __init__(self, path: str):
        self.path = path
        
    def execute(self, input: any):
        with open(self.path, "w") as f:
            f.write(str(input))
        self.result = input


