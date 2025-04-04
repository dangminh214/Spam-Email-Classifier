import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

def import_datasets() -> pd.DataFrame: 
    PATH_DATASET = "datasets/email.csv"
    df = pd.read_csv(PATH_DATASET)
    return df

def preprocessing(df) -> pd.DataFrame:
    # Drop the last unrestful element
    value = df.iloc[-1, 0]
    df.drop(df[df['Category'] == value].index, inplace = True)
    return df

# Use your custom data to make prediction
def predict_spam_or_ham(text):
    text_tfidf = vectorizer.transform([text])
    prediction = nb_model.predict(text_tfidf)
    return 'spam' if prediction == 1 else 'ham'

if __name__ == "__main__":
    df = import_datasets()
    df = preprocessing(df)
    df['Category'].unique() 

    # Clean the text: lowercase and remove punctuations
    df['Message'] = df['Message'].str.lower().str.replace(r'[^\w\s]', '')

    # Convert labels into numeric {0 : ham, 1 : spam}
    df['Category'] = df['Category'].map({'ham' : 0, 'spam' : 1})

    print(df.head())

    # Split the dataset into train, test split
    X = df['Message']
    y = df['Category']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

    # verify shapes
    print(X_train.shape)
    print(X_test.shape)
    print(y_train.shape)
    print(y_test.shape)

    # Convert text into numbers
    from sklearn.feature_extraction.text import TfidfVectorizer

    # Convert text data into numeric vectors using TFIDF
    vectorizer = TfidfVectorizer(stop_words = 'english')
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)

    # Initialize the model
    nb_model = MultinomialNB()

    # Train the model
    nb_model.fit(X_train_tfidf, y_train)

    # Make predictions
    y_pred = nb_model.predict(X_test_tfidf)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy: {accuracy * 100:.2f}%')

    # Print detailed classification report (precision, recall, F1-score)
    print(classification_report(y_test, y_pred, target_names=['ham', 'spam']))

    # Generate confusion matrix
    cm = confusion_matrix(y_test, y_pred)

    # Plot the confusion matrix
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['ham', 'spam'], yticklabels=['ham', 'spam'])
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.title('Confusion Matrix')
    plt.show()

    # Example 1: usage
    email = "Congratulations, you've won a lottery of $1000! Call now."
    result = predict_spam_or_ham(email)
    print(f"The email is: {result}")

    # Example 2: usage
    email = "I will go there any fight back!"
    result = predict_spam_or_ham(email)
    print(f"The email is: {result}")


