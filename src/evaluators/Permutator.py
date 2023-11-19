import copy
from src.modules import Utilities

from src.tools.Sequential import Sequential


class Permutator:
    permutations = []

    def __init__(self, transcribe_posibilities: list, text_filter_posibilities: list, prompting_posibilities: list,
                 topic_detection_posibilities: list):
        for transcribe in transcribe_posibilities:
            for text_filter in text_filter_posibilities:
                for prompting in prompting_posibilities:
                    for topic_detection in topic_detection_posibilities:
                        self.permutations.append(Sequential(
                            copy.copy(transcribe),
                            copy.copy(Utilities.SplitModule(separator=" ")),
                            *[copy.copy(text) for text in text_filter],
                            Utilities.JoinModule(separator=" "),
                            copy.copy(prompting),
                            copy.copy(topic_detection),
                            Utilities.JoinModule(separator="\n"),
                        ))
