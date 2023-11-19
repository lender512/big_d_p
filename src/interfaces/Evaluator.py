from __future__ import annotations

from abc import ABC


class Evaluator(ABC):
    name: str = ""

    def __init__(self):
        self.name = self.__class__.__name__

    def evaluate(self, *args):
        pass
