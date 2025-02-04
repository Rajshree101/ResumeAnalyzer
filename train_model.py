from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib
import numpy as np

# Example training data: [experience, num_skills, education_score] and their corresponding ranks
X = np.array([[5, 10, 2], [3, 5, 1], [8, 12, 3], [2, 8, 1]])  # Example features
y = np.array([1, 2, 1, 2])  # Example ranks (1, 2 are different ranks)

# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, "model/resume_ranking_model.pkl")
