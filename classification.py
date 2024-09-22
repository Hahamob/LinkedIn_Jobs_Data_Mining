import pandas as pd
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# load data
file_path = 'sorted_job_frequency.csv'
data = pd.read_csv(file_path)

# create demand_level
# Set the frequency threshold to 500. Those above this threshold are considered high demand (1), and others are low demand (0).
threshold = 500
data['demand_level'] = (data['frequency'] > threshold).astype(int)

# Use frequency as a feature to predict demand_level
X = data[['frequency']]  # Features
y = data['demand_level']  # Target variable

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the classifier
classifier = RandomForestClassifier(n_estimators=100, random_state=42)

#  Train the classifier
classifier.fit(X_train, y_train)

#  Predict on the test set
y_pred = classifier.predict(X_test)

#  Evaluate the classifier
print("Classification Report:")
print(classification_report(y_test, y_pred))
print("Accuracy Score:", accuracy_score(y_test, y_pred))
