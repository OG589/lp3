import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error,
r2_score
df = pd.read_csv("/home/student/Downloads/uber.csv")
df.head()

# Drop rows with missing values
df = df.dropna()
# Remove invalid fare values
df = df[df['fare_amount'] > 0]
# Limit passenger count
df = df[(df['passenger_count'] > 0) & (df['passenger_count'] <= 6)]
# Calculate distance using coordinates (Haversine formula)
def haversine_distance(lat1, lon1, lat2, lon2):
R = 6371 # Radius of Earth in km
phi1, phi2 = np.radians(lat1), np.radians(lat2)
dphi = np.radians(lat2 - lat1)
dlambda = np.radians(lon2 - lon1)
a = np.sin(dphi/2)**2 +
np.cos(phi1)*np.cos(phi2)*np.sin(dlambda/2)**2
return R * (2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a)))
df['distance_km'] = haversine_distance(df['pickup_latitude'],
df['pickup_longitude'],df['dropoff_latitude'],
df['dropoff_longitude'])
# Remove zero-distance rides
df = df[df['distance_km'] > 0]
# Remove outliers in fare and distance
df = df[(df['fare_amount'] < 100) & (df['distance_km'] < 50)]
plt.figure(figsize=(8,4))
sns.boxplot(x=df['fare_amount'])
plt.title("Fare Amount Distribution")
plt.show()

plt.figure(figsize=(6, 4))
sns.heatmap(df[['fare_amount', 'distance_km',
'passenger_count']].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

X = df[['distance_km', 'passenger_count']]
y = df['fare_amount']
X_train, X_test, y_train, y_test = train_test_split(X, y,
test_size=0.2, random_state=42)
lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)
def evaluate_model(y_true, y_pred, model_name):
rmse = np.sqrt(mean_squared_error(y_true, y_pred))
mae = mean_absolute_error(y_true, y_pred)
r2 = r2_score(y_true, y_pred)
print(f"{model_name} Performance:")
print(f"R² Score : {r2:.4f}")
print(f"RMSE : {rmse:.4f}")
print(f"MAE : {mae:.4f}")
print("-" * 30)
evaluate_model(y_test, y_pred_lr, "Linear Regression")
evaluate_model(y_test, y_pred_rf, "Random Forest Regression")
