# Spam Email Classifier  

A simple Machine Learning project to classify spam email and normal email. This project is to understand basic concepts of NLP and deploy a model on a server using fastapi and interact with HTML UI

## Dataset

This project utilizes the [Spam Emails Dataset](https://www.kaggle.com/datasets/ashfakyeafi/spam-email-classification/data), a dataset in machine learning that contains many samples of Emails and messages, each classifier into two classes: ham(for legit email) and spam (for spam email)

## Installation & Setup

### Prerequisites
- Python 3.8+  
- FastAPI  
- Scikit-learn  
- Pandas
- HTML 
  
### Running Steps Locally
1. **Clone the repository**  
   Clone the project repository to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Install dependencies**  
   Install the required Python dependencies.
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the FastAPI server**  
   Run the FastAPI server to serve the model (default port 8000).
   ```bash
   127.0.0.1:8000
   ```
   ```bash
   uvicorn server:app --reload
   ```

4. **Access API Documentation**  
   Open the following API documentation in your browser:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8888/docs)
   - Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8888/redoc)

5. **Run the client-side application**  
   Open web/index.html in web browser

## API Endpoints

### **POST** `/predict`

Predicts the E-Mail if it is a Spam E-Mail or not

- **Request Body (JSON):**
  ```json
  {
    "text": "Hi I am Minh"
  }
  ```
- **Response:**
  ```json
  {
    "prediction": "ham"
  }
  ```

### **GET** `/`

Give the information of project to user

- **Response:**
  ```json
  {
    "info": "Welcome to Dang Minh EMail Spam Classifier Model, this is a personal project to practice my knowledge in NLP and MLops"
  }
  ```


## Contributing

Contributions are welcome! If you find any issues or want to suggest improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
