import joblib

# Load trained model
model = joblib.load("fake_review_model.pkl")

# Load TF-IDF vectorizer
vectorizer = joblib.load("tfidf_vectorizer.pkl")


# Prediction function
def predict_review(review):

    # Convert review into TF-IDF features
    review_vector = vectorizer.transform([review])

    # Predict
    prediction = model.predict(review_vector)[0]

    # Convert prediction into label
    if prediction == 0:
        return "Fake Review (CG)"
    else:
        return "Genuine Review (OR)"


# Get review from user
review = input("Enter a product review: ")

# Display result
result = predict_review(review)

print("\nReview:", review)
print("Prediction:", result)
