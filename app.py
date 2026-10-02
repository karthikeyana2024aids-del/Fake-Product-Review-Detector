import streamlit as st
import joblib


# Load trained model
model = joblib.load("src/fake_review_model.pkl")

# Load TF-IDF vectorizer
vectorizer = joblib.load("src/tfidf_vectorizer.pkl")


# Page configuration
st.set_page_config(
    page_title="Fake Product Review Detector",
    page_icon="🕵️",
    layout="centered"
)


# Title
st.title("🕵️ Fake Product Review Detector")

st.write(
    "Enter a product review below and the machine learning model "
    "will predict whether the review is Fake or Genuine."
)


# Review input
review = st.text_area(
    "Enter Product Review:",
    placeholder="Example: This product is amazing and works perfectly!"
)


# Detect button
if st.button("🔍 Detect Review"):

    if review.strip() == "":
        st.warning("Please enter a review.")

    else:
        # Convert review into TF-IDF features
        review_vector = vectorizer.transform([review])

        # Make prediction
        prediction = model.predict(review_vector)[0]

        # Get prediction probability
        probability = model.predict_proba(review_vector)[0]

        # Display result
        if prediction == 0:
            confidence = probability[0] * 100

            st.error("🚨 Fake Review (CG)")

        else:
            confidence = probability[1] * 100

            st.success("✅ Genuine Review (OR)")

        st.metric(
            "Prediction Confidence",
            f"{confidence:.2f}%"
        )
        