from collections import OrderedDict
from src.interfaces.Module import Module

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

    def forward(self, input):
        self.input = input
        currentModule = self.startModule
        while currentModule is not None:
            print(f"Executing {currentModule.name}")
            currentModule.execute(self.input)
            self.input = currentModule.result
            currentModule = currentModule.next
        return self.input

    def __call__(self, input):
        return self.forward(input)