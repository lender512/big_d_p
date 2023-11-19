from src.interfaces.Module import Module


class JoinModule(Module):
    def __init__(self, next: Module = None, separator: str = " "):
        super().__init__(next)
        self.separator = separator
        self.config = {
            'separator': separator
        }
        
    def execute(self, input: list):
        self.result = self.separator.join(input)

class SplitModule(Module):
    def __init__(self, next: Module = None, separator: str = " "):
        super().__init__(next)
        self.separator = separator
        self.config = {
            'separator': separator
        }
        
    def execute(self, input: str):
        self.result = input.split(self.separator)

    