# 🕵️ Fake Product Review Detector

A Machine Learning based web application that detects whether a product review is **Fake or Genuine** using Natural Language Processing (NLP).

## 🚀 Live Demo

🔗 https://fakereviewdetectorkasu.streamlit.app/

---

## 📌 Project Overview

Fake product reviews can mislead customers and influence purchasing decisions.

This project uses **TF-IDF Vectorization** and **Logistic Regression** to analyze product review text and classify it into two categories:

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