from model import SpamClassifier
from sklearn.model_selection import train_test_split
from test_email import emails

if __name__ == "__main__":
    clf = SpamClassifier()

    df = clf.import_datasets()
    df = clf.preprocess(df)

    X = df['Message']
    y = df['Category']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    clf.train(X_train, y_train)

    clf.evaluate(X_test, y_test)

    # Classifier Classes: "ham" "spam"
    for email in emails:
        print(f"Email: \"{email}\" => Prediction: {clf.predict(email)}")

    # Export model and vectorizer
    clf.export('spam_classifier_model.pkl', 'tfidf_vectorizer.pkl')
