from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import os, joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)
MODEL_PATH = 'model_files/model.pkl'
VECT_PATH = 'model_files/vectorizer.pkl'

def train_or_load_model(csv_path='fruit_feedback.csv'):
    os.makedirs('model_files', exist_ok=True)
    if os.path.exists(MODEL_PATH) and os.path.exists(VECT_PATH):
        clf = joblib.load(MODEL_PATH)
        vect = joblib.load(VECT_PATH)
        le = joblib.load('model_files/label_encoder.pkl')
        return clf, vect, le

    df = pd.read_csv(csv_path).dropna()
    le = LabelEncoder()
    y = le.fit_transform(df['Satisfaction'])
    vect = TfidfVectorizer(stop_words='english', max_features=500)
    X_text = vect.fit_transform(df['FeedbackText']).toarray()
    X_num = df[['Freshness','Price','Quality','Service']].values
    X = np.hstack((X_text, X_num))

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    joblib.dump(clf, MODEL_PATH)
    joblib.dump(vect, VECT_PATH)
    joblib.dump(le, 'model_files/label_encoder.pkl')
    return clf, vect, le

clf, vect, le = train_or_load_model()

@app.route('/')
def index():
    fruits = ['Apple','Banana','Mango','Orange','Grapes','Watermelon','Pineapple','Strawberry','Papaya','Guava']
    return render_template('index.html', fruits=fruits)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    feedback = data.get('FeedbackText', '')
    try:
        freshness = float(data.get('Freshness', 5))
        price = float(data.get('Price', 5))
        quality = float(data.get('Quality', 5))
        service = float(data.get('Service', 5))
    except ValueError:
        return jsonify({'error':'Numeric fields must be numbers.'}),400

    X_text = vect.transform([feedback]).toarray()
    X_num = np.array([[freshness, price, quality, service]])
    X = np.hstack((X_text, X_num))
    pred = clf.predict(X)[0]
    label = le.inverse_transform([pred])[0]
    return jsonify({'prediction': label})

if __name__ == '__main__':
    app.run(debug=True)
