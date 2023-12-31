from src.interfaces.Module import Module
from src.tools.LlmChatOpenaiApi import LlmChatOpenaiApi
from src.tools.LlmLegacyOpenaiApi import LlmLegacyOpenaiApi


class GptApiModule(Module):
    INPUT_LLM_TEMPERATURE = 0.0

    def __init__(self, GptApi, model, tokens, next=None):
        super().__init__(next)
        self.model = model
        self.tokens = tokens
        self.GptApi = GptApi
        self.config = {
            'model': model,
        }

    def execute(self, prompts):
        self.result = []
        for prompt in prompts:
            self.result.append(self.GptApi.complete(
                model=self.model,
                purpose=prompt["purpose"],
                body=prompt["body"],
                tokens=self.tokens,
                temperature=GptApiModule.INPUT_LLM_TEMPERATURE
            ))
