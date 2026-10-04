# 🕵️ Fake Product Review Detector

A Machine Learning based web application that detects whether a product review is **Fake or Genuine** using Natural Language Processing (NLP).

## 🚀 Live Demo

🔗 https://fakereviewdetectorkasu.streamlit.app/

---

## 📌 Project Overview

Fake product reviews can mislead customers and influence purchasing decisions.

This project uses **TF-IDF Vectorization** and a **Logistic Regression** machine learning model to analyze product review text and classify it into two categories:

- 🚨 **Fake Review (CG)**
- ✅ **Genuine Review (OR)**

The application provides the predicted class along with the **prediction confidence percentage** through an interactive Streamlit web interface.

---

## ✨ Features

- 📝 Enter any product review
- 🔍 Detect whether the review is Fake or Genuine
- 📊 Display prediction confidence
- 🧹 NLP-based text preprocessing
- 🔤 TF-IDF feature extraction
- 🤖 Logistic Regression classification
- 🌐 Interactive Streamlit web interface
- ☁️ Deployed using Streamlit Cloud

---

## 🧠 Machine Learning Workflow

```text
Product Review
      ↓
Text Preprocessing
      ↓
TF-IDF Vectorization
      ↓
Logistic Regression
      ↓
Prediction
      ↓
Fake / Genuine

---

## 🧠 Machine Learning Workflow

```text
Product Review
      ↓
Text Preprocessing
      ↓
TF-IDF Vectorization
      ↓
Logistic Regression
      ↓
Prediction
      ↓
Fake / Genuine
```text

---

📸 Application Screenshots
🚨 Fake Review Detection
 
✅ Genuine Review Detection
 
🎯 Genuine Review with High Confidence

---
 
🛠️ Technologies Used
- Python
- Pandas
- Scikit-learn
- Natural Language Processing (NLP)
- TF-IDF Vectorization
- Logistic Regression
- Streamlit
- Jupyter Notebook
- Git & GitHub
- Streamlit Cloud

---

📂 Project Structure
Fake-Product-Review-Detector/
│
├── data/
│   └── fake_reviews.csv
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   └── 02_preprocessing.ipynb
│
├── screenshots/
│   ├── Fake Review Detection.png
│   ├── Genuine Review Detection.png
│   └── Genuine Review with High Confidence.png
│
├── src/
│   └── 03_prediction.py
│
├── fake_review_model.pkl
├── tfidf_vectorizer.pkl
├── test_data.py
├── app.py
├── requirements.txt
├── .gitignore
└── README.md

---

⚙️ How It Works
1. Text Preprocessing
The entered product review is cleaned and prepared for machine learning analysis.
2. TF-IDF Vectorization
The processed review text is converted into numerical feature vectors using TF-IDF (Term Frequency–Inverse Document Frequency).
3. Logistic Regression
The TF-IDF features are passed to the trained Logistic Regression model for classification.
4. Prediction
The model predicts whether the review is:
- 🚨 Fake Review (CG)
- ✅ Genuine Review (OR)
5. Confidence Score
The application displays the model's prediction confidence as a percentage.

---

▶️ Run Locally
Clone the Repository
git clone https://github.com/karthikeyana2024aids-del/Fake-Product-Review-Detector.git

Navigate to the Project Folder
cd Fake-Product-Review-Detector

Create a Virtual Environment
python -m venv venv

Activate the Virtual Environment
Windows:
venv\Scripts\activate

Install Required Packages
pip install -r requirements.txt

Run the Streamlit Application
streamlit run app.py

The application will open in your browser.

---

📊 Model Details
Component	Technology
Problem Type	Binary Text Classification
Feature Extraction	TF-IDF
Machine Learning Algorithm	Logistic Regression
Input	Product Review Text
Output	Fake / Genuine
Confidence	Prediction Probability

---

☁️ Deployment
The application is deployed using Streamlit Cloud.
🌐 Live Application
🔗 https://fakereviewdetectorkasu.streamlit.app/
🔮 Future Enhancements
- 📈 Improve model accuracy using larger datasets
- 🤖 Experiment with advanced NLP models
- 🌍 Add multiple language support
- 😊 Add review sentiment analysis
- 📊 Add probability visualization
- 📁 Add batch prediction using CSV files
- 🧠 Explore transformer-based NLP models

---

👨‍💻 Author
Karthikeyan Anandharaj
Machine Learning & Data Science Project