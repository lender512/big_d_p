from src.interfaces.Module import Module
from src.tools.LlmChatOpenaiApi import LlmChatOpenaiApi
from src.tools.LlmLegacyOpenaiApi import LlmLegacyOpenaiApi

class ChatGptApiModule(Module):
    INPUT_LLM_TEMPERATURE = 0.0

    def __init__(self, GptApiModule, model, tokens, next = None):
        super().__init__(next)
        self.model = model
        self.tokens = tokens
        self.GptApiModule = GptApiModule

    def execute(self, prompt):
        result = self.GptApiModule(
            model = self.model,
            purpose=prompt["purpose"],
            body=prompt["body"],
            tokens=self.tokens,
            temperature= ChatGptApiModule.INPUT_LLM_TEMPERATURE
        )
        self.result = result

