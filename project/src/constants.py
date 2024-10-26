import os
from enum import Enum


class SentimentLabel(str, Enum):
    NEGATIVE = "NEGATIVE"
    NEUTRAL = "NEUTRAL"
    POSITIVE = "POSITIVE"


LABEL_CLASS_TO_NAME = {
    0: SentimentLabel.NEGATIVE.value,
    1: SentimentLabel.NEUTRAL.value,
    2: SentimentLabel.POSITIVE.value,
}


# TODO: Add your model name from the WANDB Model Registry
# It should look like this
# "yudhiesh/model-registry/Drugs Review MLOps Uplimit:v1"
WANDB_MODEL_REGISTRY_MODEL_NAME = "stefansturlu-sidekick-health/model-registry/review-sentiment-analysis-dev:v0"
# "stefansturlu-sidekick-health/Drug Review MLOps Uplimit/run-9npfqtx4-logreg_model_LR_train_size_1000.onnx:v1"

# NOTE: Ensure that you set the API Key within Github Codespaces secrets
# in the settings page of your repository!
WANDB_API_KEY = os.getenv("WANDB_API_KEY")
