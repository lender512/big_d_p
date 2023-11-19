import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import openai
from src.evaluators.Permutator import Permutator
from src.evaluators.TopicModelling import TopicModelling
from src.modules import Transcribe, TextFilter, Prompting, TopicDetection
from src.tools.LlmChatOpenaiApi import LlmChatOpenaiApi

openai.api_key = 'API_KEY'

if __name__ == "__main__":
    audio = "PLANICIE NOTICIAS - RADIO PLANICIE  13-09-2023"
    audio_input = f"data/audios/{audio}.mp3"
    audio_reference = f"reference_output/{audio}.txt"

    perm = Permutator(
        transcribe_posibilities=[
            Transcribe.WhisperApiModule(),
            Transcribe.WhisperLocalModule("tiny", "Spanish", False)
        ],
        text_filter_posibilities=[
            (TextFilter.LowerCase(), TextFilter.FuzzyClean(threshold=0.9)),
            (TextFilter.LowerCase(), TextFilter.FuzzyClean(threshold=0.9), TextFilter.RemoveStopWords(),
             TextFilter.RemoveNonExistingWords()),
            (TextFilter.LowerCase(), TextFilter.FuzzyClean(threshold=0.9), TextFilter.RemoveStopWords(),
             TextFilter.RemoveNonExistingWords(), TextFilter.TfIdfFilter(threshold=0.1))
        ],
        prompting_posibilities=[
            Prompting.PromptingModule("simple"),
            Prompting.PromptingModule("verbose")
        ],
        topic_detection_posibilities=[
            TopicDetection.GptApiModule(LlmChatOpenaiApi, "gpt-3.5-turbo", 1024),
            TopicDetection.GptApiModule(LlmChatOpenaiApi, "gpt-4-1106-preview", 1024),
        ]
    )

    evaluator = TopicModelling()
    for permutation in perm.permutations:
        evaluator.evaluate(permutation, audio_input, audio_reference)
        print('---------------------------------------------------')
