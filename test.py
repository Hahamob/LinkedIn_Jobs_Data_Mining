from sklearn.model_selection import train_test_split
# Load the dataset
file_path = 'clustered_data.csv'
data = pd.read_csv(file_path)

#  'frequency' is the target variable
X = data.drop('frequency', axis=1)  # Features
y = data['frequency']  # Target variable

# Perform the split with a 70/30 ratio
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Now you have your training set (X_train, y_train) and your testing set (X_test, y_test)
