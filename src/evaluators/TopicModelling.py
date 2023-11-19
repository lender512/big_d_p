from src.interfaces.Evaluator import Evaluator
from src.tools.Sequential import Sequential
from datetime import datetime
from rouge_score import rouge_scorer
import json


class TopicModelling(Evaluator):
    def __init__(self):
        super().__init__()

    def evaluate(self, pipeline: Sequential, filename: str, reference_filename):
        # 1
        timestamp = datetime.now()

        # 2
        configs = []
        copy_pointer = pipeline.startModule
        config = copy_pointer.config
        config["name"] = copy_pointer.__class__.__name__
        configs.append(config)

        while copy_pointer.next is not None:
            copy_pointer = copy_pointer.next
            config = copy_pointer.config
            config["name"] = copy_pointer.__class__.__name__
            configs.append(config)

        scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)

        value = pipeline(filename)
        endTime = datetime.now()
        reference_text_all = open(reference_filename, "r").read()

        scores = scorer.score(reference_text_all, value)

        final = {
            "timestamp": timestamp.strftime("%m/%d/%Y, %H:%M:%S"),
            "configs": configs,
            "scores": {
                'rouge1': {
                    'fmeasure': scores['rouge1'].fmeasure,
                    'precision': scores['rouge1'].precision,
                    'recall': scores['rouge1'].recall
                },
                'rougeL': {
                    'fmeasure': scores['rougeL'].fmeasure,
                    'precision': scores['rougeL'].precision,
                    'recall': scores['rougeL'].recall
                }
            },
            "value": value,
            "time": (endTime - timestamp).total_seconds()
        }

        with open(f"data/results/{timestamp}.json", "w") as f:
            json.dump(final, f)
