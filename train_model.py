# train_model.py

import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
import joblib

# Load CSV
data = pd.read_csv(r"C:\Users\mahes\Desktop\emp_using_knn\Dataset09-Employee-salary-prediction.csv")

# Fill missing numeric values with mean
data = data.fillna(data.mean(numeric_only=True))

# Drop any remaining rows with nulls (usually from categorical columns)
data = data.dropna()

# Encode categorical columns
le_gender = LabelEncoder()
le_edu = LabelEncoder()
le_job = LabelEncoder()

data['Gender_Encode'] = le_gender.fit_transform(data['Gender'])
data['Degree_Encode'] = le_edu.fit_transform(data['Education Level'])
data['Job_Title_Encode'] = le_job.fit_transform(data['Job Title'])

# Scale numeric features
scaler = StandardScaler()
data['Age_scaled'] = scaler.fit_transform(data[['Age']])
data['Exp_scaled'] = scaler.fit_transform(data[['Years of Experience']])

# Features and label
X = data[['Age_scaled', 'Gender_Encode', 'Degree_Encode', 'Job_Title_Encode', 'Exp_scaled']]
y = data['Salary']

# Train-test split
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train KNN model
model = KNeighborsRegressor(n_neighbors=3)
model.fit(x_train, y_train)

# Save model and scaler
joblib.dump(model, 'model_knn.pkl')
joblib.dump(scaler, 'scaler.pkl')
