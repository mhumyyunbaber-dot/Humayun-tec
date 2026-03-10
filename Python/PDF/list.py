import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

#  Load dataset
iris = load_iris(as_frame=True)

# Convert to DataFrame
df = iris.frame

print("First 5 rows of dataset:")
print(df.head())


# Separate features and target
X = df.drop("target", axis=1)
y = df["target"]

print(df.shape)
# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


model = LogisticRegression(
    max_iter=200,  # ensure convergence
    solver='lbfgs' 
)

# Train the model
model.fit(X_train, y_train)


#  Make predictions
predictions = model.predict(X_test)

# Evaluate model
accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", accuracy)

print("Confusion Matrix:")
print(confusion_matrix(y_test, predictions))

print("Classification Report:")
print(classification_report(y_test, predictions))
import pandas as pd

# Create sample data
data = {
    'name': ['John', 'Jane', 'Bob'],
    'age': [25, 30, 35],
    'city': ['NYC', 'LA', 'Chicago']
}

# Save as CSV
df = pd.DataFrame(data)
df.to_csv('sales.csv', index=False)

# Now read it
df = pd.read_csv('sales.csv')
print(df)