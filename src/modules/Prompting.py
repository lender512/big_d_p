from src.interfaces.Module import Module

class PromptingModule(Module):
    def __init__(self, mode, chunk_size = 1024, next = None):
        super().__init__(next)
        self.config = {
            'mode': mode,
            'chunk_size': chunk_size,
            'name': self.__class__.__name__
        }
        self.module = mode
        self.chunk_size = chunk_size
        if mode == "simple":
            self.purpose = "TAREA: Resume el texto de entrada en puntos clave."
        elif mode == "verbose":
            self.purpose = "TAREA: Analiza la transcripción y señala los tópicos específicos que fueron discutidos con mayor énfasis en puntos clave."
        elif mode == "autocritic":
            self.purpose = "TAREA: Analiza el texto inicial y reescribe los topicos detectados, añade temas de ser necesario."
            raise Exception("Mode not implemented")
        else:
            raise Exception("Invalid mode")
    
    def split_text_into_chunks(text, chunk_size):
        words = text.split()
        chunks = []
        current_chunk = ""
        
        for word in words:
            if len(current_chunk.split()) + len(word.split()) <= chunk_size:
                current_chunk += " " + word
            else:
                chunks.append(current_chunk.strip())
                current_chunk = word

        if current_chunk:
            chunks.append(current_chunk.strip())

        return chunks

    def execute(self, text):
        if self.module == "autocritic":
            initial_chunks = text['ctx']['initial_chunks']
            prev_chunks = text['ctx']['prev_chunks']
            self.result = []
            for initial_chunk, prev_chunk in zip(initial_chunks, prev_chunks):
                self.result.append( {
                    "purpose": self.purpose,
                    "body": f"""
                    * TEXTO INICIAL: {initial_chunk}
                    * TOPICOS DETECTADOS: {prev_chunk}
    """
                })
        else:
            chunks = PromptingModule.split_text_into_chunks(text, self.chunk_size)
            self.result = []
            for chunk in chunks:
                self.result.append( {
                    "purpose": self.purpose,
                    "body": chunk
                })