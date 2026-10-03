# Aim: To demonstrate data loading, splitting, model training
# and evaluation using Scikit-learn.

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1. Load dataset
iris = load_iris()
X = iris.data
y = iris.target

print("Dataset Features:", iris.feature_names)
print("Target Classes:", iris.target_names)
print("Total Records:", len(X))

# 2. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Train model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# 4. Make predictions
predictions = model.predict(X_test)

# 5. Evaluate model
print("\nAccuracy:", accuracy_score(y_test, predictions))
print("\nClassification Report:")
print(classification_report(
    y_test, predictions, target_names=iris.target_names
))

# 6. Predict a new sample
sample = [[5.1, 3.5, 1.4, 0.2]]
result = model.predict(sample)[0]
print("Predicted Class:", iris.target_names[result])