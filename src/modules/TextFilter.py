from __future__ import annotations
from collections import OrderedDict
from fuzzywuzzy import fuzz
import nltk
from src.interfaces.Module import Module
from sklearn.feature_extraction.text import TfidfVectorizer 
import numpy as np

class UpperCase(Module):
    def execute(self, input: list[str]):
        self.result = [word.upper() for word in input]

class LowerCase(Module):
    def execute(self, input: list[str]):
        self.result = [word.lower() for word in input]

class FuzzyClean(Module):
    threshold = 0.9

    def __init__(self, next: Module = None, threshold: float = 0.9):
        super().__init__(next)
        self.threshold = threshold


    def execute(self, input: list[str]):
        filtered_words = []
        for i in range(len(input)-1):
            score = fuzz.ratio(input[i], input[i+1])
            filtered_words.append(input[i]) if score < self.threshold*100 else None
        self.result =  filtered_words


class RemoveStopWords(Module):
    nltk.download('stopwords')
    stopword_es = nltk.corpus.stopwords.words('spanish')

    def execute(self, input: list[str]):
        filtered_words = []
        for word in input:
            if word not in self.stopword_es:
                filtered_words.append(word)
        self.result = filtered_words

class RemoveNonExistingWords(Module):
    nltk.download('cess_esp')
    stopword_es = set(nltk.corpus.cess_esp.words())

    def execute(self, input: list[str]):
        filtered_words = []
        for word in input:
            if word in self.stopword_es:
                filtered_words.append(word)
        self.result = filtered_words


class TfIdfFilter(Module):
    def __init__(self, next: Module = None, threshold: float = 0.9):
        super().__init__(next)
        self.threshold = threshold

    def execute(self, input: list[str]):
        vectorizer = TfidfVectorizer() 
        train_tf = vectorizer.fit(input) 
        idf_scores = train_tf.idf_

        # Normalize IDF scores
        max_idf = np.max(idf_scores)
        normalized_idf = idf_scores / max_idf

        filtered_indices = np.argwhere(normalized_idf > self.threshold)
        filtered_indices = [idx[0] for idx in filtered_indices]

        # List of vocabulary from the vectorizer
        vocabulary = train_tf.get_feature_names_out()
        filtered_voc = {vocabulary[i] for i in filtered_indices}
        filtered_text_list = []
        
        for text in input:
            text_word_list = [word for word in text.split() if word in filtered_voc]
            if text_word_list:
                filtered_text_list.append(' '.join(text_word_list))
                
        self.result = filtered_text_list


