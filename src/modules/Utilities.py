from src.interfaces.Module import Module


class JoinModule(Module):
    def __init__(self, next: Module = None, separator: str = " "):
        super().__init__(next)
        self.separator = separator
        
    def execute(self, input: list):
        self.result = self.separator.join(input)

    