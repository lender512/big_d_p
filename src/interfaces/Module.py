from __future__ import annotations

from abc import ABC


class Module(ABC):
    name: str = ""
    next: Module = None
    result: any = None
    config: dict = {}

    def __init__(self, next: Module = None):
        self.name = self.__class__.__name__
        self.next = next

    def execute(self, *args):
        pass
