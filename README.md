# 📩 SMS Spam Classification

A Machine Learning + Streamlit web application that classifies SMS messages as Spam or Ham (Not Spam). This project uses a trained ML model and TF-IDF vectorizer to predict whether a given SMS is spam. 

## 🚀 Features

✅ Upload or enter an SMS message and check if it’s Spam or Ham
✅ Built using Scikit-learn for model training
✅ TF-IDF Vectorizer for text preprocessing
✅ Streamlit web app for interactive UI
✅ Lightweight and fast prediction

## ⚙️ Installation & Setup

Clone the repository:

https://github.com/J-TECH-bot/SMS_Spam-Classifier.git
cd sms-spam-classification


Create a virtual environment and activate it:

python -m venv venv
venv\Scripts\activate   # On Windows  
source venv/bin/activate  # On Mac/Linux  


Install dependencies:

pip install -r requirements.txt


Run the Streamlit app:

streamlit run app.py

## 📊 Dataset

The dataset used is spam_sms.csv, which contains labeled SMS messages categorized into:

Spam → Unwanted promotional/advertisement messages

Ham → Normal, meaningful SMS messages

## 📦 Requirements

Main libraries used:

scikit-learn 1.7.1

streamlit

pandas

numpy

(Complete list in requirements.txt)

📌 Future Improvements

Add support for multiple languages

Enhance UI with charts and analytics

Deploy on Streamlit Cloud / Heroku / Render

👨‍💻 Author

Developed by Jay Deshmukh ✨
