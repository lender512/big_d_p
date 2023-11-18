from src.interfaces.Module import Module
from src.tools.TranscribeOpenaiApi import TranscribeOpenaiApi
import whisper
from tqdm import tqdm
import numpy as np

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
    model = None
    options = None
    chunk_limit = 480000
    audios = []
    def __init__(self, model: str = "small", language: str = "Spanish", fp16: bool = False):
        self.model = whisper.load_model(model)
        self.options = whisper.DecodingOptions(language=language, fp16 = fp16)


    def execute(self, file_path: str):
        audio = whisper.load_audio(file_path)
        if audio is None:
            raise Exception("Error loading audio file")
        if len(audio) <= self.chunk_limit:
            self.audios.append(audio)
        else:
            for i in tqdm(range(0, len(audio), self.chunk_limit), desc="Processing chunks"):
                chunk = audio[i:i + self.chunk_limit]
                chunk_index = len(chunk)
                if chunk_index < self.chunk_limit:
                    padding = [0] * (self.chunk_limit - chunk_index)
                    arr1 = np.array(chunk)
                    arr2 = np.array(padding)
                    chunk = np.concatenate((arr1, arr2)).astype(np.float32)
                self.audios.append(chunk)

        results = ""

        # for audio in self.audios:
        for audio in tqdm(self.audios, desc="Processing audio files", unit="audio"):
            mel = whisper.log_mel_spectrogram(audio).to(self.model.device)
            result = whisper.decode(self.model, mel, self.options)
            results += result.text


        self.result = results