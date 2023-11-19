import copy
from Sequential import Sequential
from src.modules import Transcribe, TextFilter, Prompting, TopicDetection, Utilities
import pickle

class Permutator:
    _permutations = []
    current_permutation = None
    def __init__(self, transcribe_posibilities: list, text_filter_posibilities: list, prompting_posibilities: list, topic_detection_posibilities: list):
        i = 0
        for transcribe in transcribe_posibilities:
            for text_filter in text_filter_posibilities:
                for prompting in prompting_posibilities:
                    for topic_detection in topic_detection_posibilities:
                        print(f"Generating permutation {i}")
                        self._permutations.append(Sequential(
                            copy.copy(transcribe),
                            copy.copy(Utilities.SplitModule(separator=" ")),
                            *[copy.copy(text) for text in text_filter],
                            Utilities.JoinModule(separator=" "),
                            copy.copy(prompting),
                            copy.copy(topic_detection)
                        ))
                        i += 1
    def next_permutation(self):
        if len(self._permutations) > 0:
            self.current_permutation = self._permutations.pop()
            #save self_permutations as pickle
            with open('self_permutations.pkl', 'wb') as f:
                pickle.dump(self._permutations, f)
        else:
            self.current_permutation = None