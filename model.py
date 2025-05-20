import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# Load and preprocess data
df = pd.read_csv('calories_burnt.csv')
df.columns = df.columns.str.strip()
df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})

X = df.drop(['ID', 'Calories'], axis=1)
y = df['Calories']

# Split the data for model evaluation
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train the model
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# Predict on the test set for metrics
y_pred_test = model.predict(X_test_scaled)
r2 = r2_score(y_test, y_pred_test)
mae = mean_absolute_error(y_test, y_pred_test)
mse = mean_squared_error(y_test, y_pred_test)
rmse = np.sqrt(mse)

# Predict function with metrics
def predict_calories(gender, age, height, weight, duration, heart_rate, body_temp):
    input_df = pd.DataFrame([{
        'Gender': gender,
        'Age': age,
        'Height(cm)': height,
        'Weight(kg)': weight,
        'Duration(min)': duration,
        'Heart_Rate': heart_rate,
        'Body_Temp(C)': body_temp
    }])
    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)[0]

    return prediction, r2, mae, mse, rmse
