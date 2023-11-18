from src.interfaces.Module import Module
from src.tools.LlmChatOpenaiApi import LlmChatOpenaiApi
from src.tools.LlmLegacyOpenaiApi import LlmLegacyOpenaiApi

class ChatGpt3ApiModule(Module):
    def execute(self, input: str):
        chat = LlmChatOpenaiApi(
            prompt = input,
            engine = "davinci",
            max_tokens = 100,
            temperature = 0.9,
            top_p = 1,
            frequency_penalty = 0.0,
            presence_penalty = 0.0,
            stop = ["\n", "Human:", "AI:"]
        )
        self.result = chat