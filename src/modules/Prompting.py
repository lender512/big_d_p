from src.interfaces.Module import Module

class Prompter(Module):
    def __init__(self, mode, next = None):
        super().__init__(next)
        if mode == "simple":
            self.purpose = "Resume el texto de entrada en puntos clave."
        elif mode == "verbose":
            self.purpose = "Analiza la transcripción y señala los tópicos específicos que fueron discutidos con mayor énfasis en puntos clave."
        elif mode == "autocritic":
            raise Exception("Mode not implemented")
        else:
            raise Exception("Invalid mode")

    def execute(self, text):
        return {
            "purpose": self.purpose,
            "body": text
        }