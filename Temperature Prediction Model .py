import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Task 1: Preprocess the data
# Load the CSV file
data = pd.read_csv('temperature.csv')

# Parse the 'Date' column as datetime
data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y %H:%M')

# Select a city for prediction, e.g., 'Eilat' (close to Egypt border, similar climate)
city = 'Eilat'

# Handle missing values: Forward fill for time series data
data[city] = data[city].ffill()

# No categorical data to transform, all numerical except Date

# Create a 'Day' column for daily aggregation
data['Day'] = data['Date'].dt.date

# Group by day to get daily average temperature
daily_data = data.groupby('Day')[city].mean().reset_index()
daily_data.columns = ['Day', 'Avg_Temp']

# Convert 'Day' to ordinal for numerical feature (days since start)
daily_data['Day_Ordinal'] = daily_data['Day'].apply(lambda x: x.toordinal())

# Task 2: Visualize the data
# Plot temperature over time
plt.figure(figsize=(12, 6))
plt.plot(daily_data['Day'], daily_data['Avg_Temp'], marker='o', linestyle='-', color='b')
plt.title('Daily Average Temperature in Eilat (Near Egypt)')
plt.xlabel('Date')
plt.ylabel('Average Temperature (K)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Insights: The plot shows seasonal variations in temperature, with peaks and troughs likely corresponding to summer and winter. There are some missing data filled, but overall trends are visible.

# Task 3: Split the data
# Features (X): Day_Ordinal, Target (y): Avg_Temp
X = daily_data[['Day_Ordinal']]
y = daily_data['Avg_Temp']

# Split into train-test (80-20, chronological since time series)
train_size = int(0.8 * len(daily_data))
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

# Task 4: Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Task 5: Evaluate the model
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:.2f}")
print(f"R² Score: {r2:.2f}")

# Plot predictions vs actual
plt.figure(figsize=(12, 6))
plt.plot(daily_data['Day'][train_size:], y_test, label='Actual', color='b')
plt.plot(daily_data['Day'][train_size:], y_pred, label='Predicted', color='r', linestyle='--')
plt.title('Actual vs Predicted Temperature in Eilat (Near Egypt)')
plt.xlabel('Date')
plt.ylabel('Average Temperature (K)')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Task 6: Document your work
# Summary:
# In this project, I preprocessed the temperature dataset by parsing dates, handling missing values with forward fill, and aggregating to daily averages for Eilat (near Egypt border). Visualization revealed clear seasonal patterns in temperature. The data was split chronologically into 80% training and 20% testing sets. A Linear Regression model was trained using day ordinal as the feature to predict average temperature. The model's performance was evaluated with MSE and R², showing a basic fit but limited accuracy due to the linear assumption on seasonal data. Insights include the cyclical nature of temperatures, suggesting more advanced models like time series forecasting (e.g., ARIMA) could improve predictions.
# Overall, this demonstrates basic data handling and modeling with NumPy, Pandas, Matplotlib, and Scikit-learn.