from src.interfaces.Module import Module
from src.tools.TranscribeOpenaiApi import TranscribeOpenaiApi

class WhisperApiModule(Module):
    INPUT_S2T_MODEL = "whisper-1"
    INPUT_AUDIO_LANGUAGE = "es"
    OUTPUT_TEXT_FORMAT = "text"

    def execute(self, file_path: str):
        with open(file_path, "rb") as audio_file:
            transcript = TranscribeOpenaiApi(
                file = audio_file,
                model = WhisperApiModule.INPUT_S2T_MODEL,
                response_format=WhisperApiModule.OUTPUT_TEXT_FORMAT,
                language=WhisperApiModule.INPUT_AUDIO_LANGUAGE
            )
        self.result = transcript


class WhisperLocalModule(Module):
    pass
