from fastapi import FastAPI
from pydantic import BaseModel
import pickle
from fastapi.middleware.cors import CORSMiddleware

# Load the pre-trained model and vectorizer
with open("spam_classifier_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("tfidf_vectorizer.pkl", "rb") as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# FastAPI app instance
app = FastAPI()

# Allow all origins to make requests (for development purposes)
origins = [
    "*",  # Allows all origins, can be restricted to specific domains in production
]

# Add CORS middleware to the FastAPI app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

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
