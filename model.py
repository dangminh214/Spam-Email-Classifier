import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

class SpamClassifier:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.model = MultinomialNB()

    def import_datasets(self, path="datasets/email.csv") -> pd.DataFrame:
        df = pd.read_csv(path)
        return df

    def preprocess(self, df: pd.DataFrame) -> pd.DataFrame:
        value = df.iloc[-1, 0]
        df.drop(df[df['Category'] == value].index, inplace=True)
        df['Message'] = df['Message'].str.lower().str.replace(r'[^\w\s]', '', regex=True)
        df['Category'] = df['Category'].map({'ham': 0, 'spam': 1})
        return df

    def train(self, X_train, y_train):
        X_train_tfidf = self.vectorizer.fit_transform(X_train)
        self.model.fit(X_train_tfidf, y_train)

    def evaluate(self, X_test, y_test):
        X_test_tfidf = self.vectorizer.transform(X_test)
        y_pred = self.model.predict(X_test_tfidf)
        acc = accuracy_score(y_test, y_pred)
        print(f"Accuracy: {acc * 100:.2f}%")
        print(classification_report(y_test, y_pred, target_names=['ham', 'spam']))
        cm = confusion_matrix(y_test, y_pred)
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['ham', 'spam'], yticklabels=['ham', 'spam'])
        plt.xlabel('Predicted')
        plt.ylabel('True')
        plt.title('Confusion Matrix')
        plt.show()

    def predict(self, text):
        text_tfidf = self.vectorizer.transform([text])
        prediction = self.model.predict(text_tfidf)
        return 'spam' if prediction == 1 else 'ham'
