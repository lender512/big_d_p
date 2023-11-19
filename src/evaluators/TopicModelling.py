from overrides import override
from src.interfaces.Evaluator import Evaluator
from src.tools.Sequential import Sequential
from datetime import datetime


class TopicModelling(Evaluator):
    def __init__(self):
        super().__init__()

    def _get_reference_topics(self, text: str):
        pass

    def _get_result_folder(self):
        return f"results/{self.name}"

    @override
    def evaluate(self, pipeline: Sequential, filename: str):
        timestamp = datetime.now()
        pass
