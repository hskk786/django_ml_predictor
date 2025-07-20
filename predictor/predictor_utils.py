import joblib
import numpy as np
import os

# --- Paths to model and encoder ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "ml_models", "student_model.pkl")

# Load the trained ML model
model = joblib.load(MODEL_PATH)

# Load performance label encoder (for decoding predictions)
le_performance = joblib.load(os.path.join(BASE_DIR, "ml_models", "le_performance.pkl"))

# Manual mappings for categorical features
gender_map = {"male": 0, "female": 1}
testprep_map = {"none": 0, "completed": 1}


def preprocess_input(gender, math_score, reading_score, writing_score, testprep, avg_score):
    """
    Convert raw form inputs into a NumPy array for prediction.
    Gender and Test Prep are mapped manually (0/1) as the model expects numeric inputs.
    """

    # Normalize input to lowercase and map to integers
    gender_encoded = gender_map[gender.strip().lower()]
    testprep_encoded = testprep_map[testprep.strip().lower()]

    # Combine features into a single array (order must match training data)
    features = np.array([
        gender_encoded,
        math_score,
        reading_score,
        writing_score,
        testprep_encoded,
    ]).reshape(1, -1)

    return features


def predict_student_performance(gender, math_score, reading_score, writing_score, testprep, avg_score):
    """
    Predict the student's performance category (e.g., "Poor", "Average", "Excellent").
    """
    # Preprocess the user input
    X = preprocess_input(gender, math_score, reading_score, writing_score, testprep, avg_score)

    # Make prediction (model outputs a numeric label)
    pred = model.predict(X)

    # Decode numeric label back to string category
    decoded_label = le_performance.inverse_transform(pred)

    return decoded_label[0]
