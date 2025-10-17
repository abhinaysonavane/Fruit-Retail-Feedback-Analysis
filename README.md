# Fruit Retail Feedback Analysis using Random Forest

A **web-based application** that predicts customer satisfaction for a fruit retail business using **Random Forest Classifier**. This project collects customer feedback (ratings and text) and automatically predicts whether the customer is **Satisfied** or **Unsatisfied**.


#**Features**

- Input customer feedback:
  - Textual comments  
  - Numeric ratings for Freshness, Price, Quality, and Service  
- Predicts Satisfaction using a Random Forest model  
- Shows predictions in a user-friendly web interface built with Flask, HTML, CSS, and JavaScript  
- Can be extended to display probabilities, trends, or key factors affecting satisfaction  


## **Project Structure**

fruit-retail-flask/
├─ app.py # Flask backend
├─ requirements.txt # Python dependencies
├─ fruit_feedback.csv # Dataset file
├─ model_files/
│ ├─ model.pkl # Trained Random Forest model
│ └─ vectorizer.pkl # TF-IDF vectorizer for text
├─ templates/
│ └─ index.html # Frontend web page
├─ static/
│ ├─ style.css # Styling
│ └─ script.js # JavaScript for form handling
└─ README.md # Project documentation

yaml
Copy code

---

## **Installation**

1. Clone the repository:

```bash
git clone https://github.com/username/fruit-retail-feedback.git
cd fruit-retail-flask
Create a virtual environment:

bash
Copy code
python -m venv venv
Activate the virtual environment:

Windows Command Prompt:

bash
Copy code
venv\Scripts\activate
Windows PowerShell:

powershell
Copy code
.\venv\Scripts\activate
macOS/Linux:

bash
Copy code
source venv/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Place your dataset fruit_feedback.csv in the project root.

Usage
Run the Flask app:

bash
Copy code
python app.py
Open your browser and go to:

cpp
Copy code
http://127.0.0.1:5000
Fill in the customer feedback form.

Click Predict to see satisfaction results.

Technologies Used
Python 3.x
Flask (Web framework)
Pandas, NumPy (Data processing)
Scikit-learn (Machine Learning: Random Forest, TF-IDF)
HTML, CSS, JavaScript (Frontend)

Purpose
This project helps fruit retailers:
Collect and analyze customer feedback efficiently
Identify areas needing improvement (price, quality, service)
Make data-driven business decisions
Improve customer satisfaction and loyalty


