from __future__ import annotations


class Module(object):
    name: str = ""
    next: Module = None
    result: any = None

    def __init__(self, next: Module = None):
        self.name = self.__class__.__name__
        self.next = next

    def execute(self, *args):
        pass