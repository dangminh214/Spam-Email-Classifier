FROM python:3.12
LABEL authors="dang-minh"

# Set the working directory in the container
WORKDIR /src

COPY spam_classifier_model.pkl /src/spam_classifier_model.pkl 
COPY tfidf_vectorizer.pkl /src/tfidf_vectorizer.pkl 
COPY server.py /src/server.py
COPY requirements.txt /src/requirements.txt

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that FastAPI will run on
EXPOSE 8888

# Run FastAPI app using uvicorn
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8888"]
