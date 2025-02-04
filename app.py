from flask import Flask, request, render_template
import os
import joblib
import numpy as np
from resume_ranking import extract_resume_data

app = Flask(__name__)

# Load the pre-trained model
model = joblib.load("model/resume_ranking_model.pkl")

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_resume():
    if request.method == "POST":
        file = request.files["resume"]
        if file:
            # Save the file temporarily
            file_path = os.path.join("uploads", file.filename)
            file.save(file_path)

            # Extract features
            experience, num_skills, education_score = extract_resume_data(file_path)

            if experience is None:  # In case feature extraction failed
                return "Failed to extract features from the resume."

            # Prepare features for prediction
            features = np.array([[experience, num_skills, education_score]])

            # Check the features before predicting
            print("Features for Prediction:", features)

            # Predict the rank using the model
            rank = model.predict(features)[0]

            # Check the predicted rank
            print("Predicted Rank:", rank)

            return f"Predicted Rank: {rank}"

if __name__ == "__main__":
    app.run(debug=True)
