from fastapi import FastAPI
from pydantic import baseModel
import torch
import os 
from transformers import AutoTokenizer, AutoModelForSequenceClassification


MODEL_PATH = "./model"

app = FastAPI(
    title = "Suicidal Text Classifier API"
    description="Detects suicidal ideation in text using a fine-tuned BERT model.",
    version="1.0.0"
)