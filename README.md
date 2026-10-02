# 🕵️ Fake Product Review Detector

A Machine Learning based web application that detects whether a product review is **Fake** or **Genuine** using Natural Language Processing (NLP).

## 📌 Project Overview

Fake product reviews can mislead customers and affect purchasing decisions.

This project uses **TF-IDF Vectorization** and Machine Learning classification algorithms to analyze product reviews and predict whether a review is:

- 🕵️ Fake Review (CG)
- ✅ Genuine Review (OR)

The trained model is deployed using **Streamlit** to provide an interactive web interface.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- TF-IDF Vectorization
- Logistic Regression
- Naive Bayes
- Random Forest
- Joblib
- Streamlit
- Matplotlib
- Jupyter Notebook

## 📂 Project Structure

```text
Fake-Product-Review-Detector/
│
├── data/
│   └── fake_reviews.csv
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   └── 02_preprocessing.ipynb
│
├── src/
│   ├── test_data.py
│   ├── 03_prediction.py
│   ├── fake_review_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── app.py
├── README.md
└── requirements.txt

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Fake-Product-Review-Detector.git
cd Fake-Product-Review-Detector


### 🔥 Then next section:

```markdown
## 🖥️ Application

The Streamlit application provides an interactive interface where users can enter a product review and detect whether it is classified as fake or genuine.

### Example 1 – Fake Review

**Input:**

> This product is absolutely amazing! Best product ever! I love it so much! Perfect quality and works perfectly!

**Prediction:** Fake Review (CG)

**Confidence:** 75.91%

### Example 2 – Genuine Review

**Input:**

> The product arrived on time. The build quality is decent and it works as expected. The battery lasts around two days with normal usage. Overall, I am satisfied with the purchase.

**Prediction:** Genuine Review (OR)

**Confidence:** 95.77%

## 🚀 Future Enhancements

- Improve model accuracy using advanced NLP techniques.
- Experiment with deep learning models such as LSTM and BERT.
- Add multilingual review detection.
- Add review sentiment analysis.
- Add a database for storing prediction history.
- Deploy the application on Streamlit Cloud.
- Add product-specific fake review analysis.

---

## 👨‍💻 Author

Developed as a Machine Learning and Natural Language Processing project.