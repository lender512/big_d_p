from src.interfaces.Module import Module

class Prompter(Module):
    def __init__(self, mode, next = None):
        super().__init__(next)
        self.module = mode
        if mode == "simple":
            self.purpose = "TAREA: Resume el texto de entrada en puntos clave."
        elif mode == "verbose":
            self.purpose = "TAREA: Analiza la transcripción y señala los tópicos específicos que fueron discutidos con mayor énfasis en puntos clave."
        elif mode == "autocritic":
            self.purpose = "TAREA: Analiza el texto inicial y reescribe los topicos detectados, añade temas de ser necesario."
            raise Exception("Mode not implemented")
        else:
            raise Exception("Invalid mode")

    def execute(self, text):
        if self.module == "autocritic":
            return {
                "purpose": self.purpose,
                "body": f"""
                * TEXTO INICIAL: {text['ctx']['initial']}
                * TOPICOS DETECTADOS: {text['prev']}
"""
            }
        else:
            return {
                "purpose": self.purpose,
                "body": text
            }