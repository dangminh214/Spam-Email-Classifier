from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

# Load the pre-trained model and vectorizer
with open("spam_classifier_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("tfidf_vectorizer.pkl", "rb") as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# FastAPI app instance
app = FastAPI()

# Request body model for email input
class Email(BaseModel):
    text: str

# Prediction endpoint
@app.post("/predict/")
def predict_spam_or_ham(email: Email):
    # Transform the text using the loaded vectorizer
    text_tfidf = vectorizer.transform([email.text])
    
    # Make a prediction using the model
    prediction = model.predict(text_tfidf)
    
    # Return the result as a dictionary
    result = "spam" if prediction == 1 else "ham"
    return {"email": email.text, "prediction": result}
