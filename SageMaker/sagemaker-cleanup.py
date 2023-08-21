#!/usr/bin/env python

from sagemaker.huggingface import HuggingFacePredictor

predictor = HuggingFacePredictor('hf-bart-large-cnn-summarization')

predictor.delete_endpoint() # This will delete the endpoint, and the endpoint configuration, but will not delete the model.