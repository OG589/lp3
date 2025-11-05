from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
df = pd.read_csv(r"C:\Users\karti\Downloads\Churn_Modelling.csv")

df.head()

Drop irrelevant columns
df = df.drop(["RowNumber"
"CustomerId", "Surname"], axis=1)
# Encode categorical columns
le_geo = LabelEncoder()
le_gender = LabelEncoder()
df["Geography"] = le_geo.fit_transform(df["Geography"])
df["Gender"] = le_gender. fit_transform(df["Gender"])

# Features (X) and Target (y)
X= df.drop("Exited", axis=1)
Y= df["Exited"]
# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2, random_state=42, stratify=y)


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

Normalize features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler. transform(X_test)
#Build Neural Network Classifier
mlp = MLPClassifier(hidden_layer_sizes=(32,16), activation="relu", solver="adam", max_iter=300, random_state=42)
mlp.fit(X_train, y_train)
y_pred = mlp.predict(X_test)

# Accuracy
acc = accuracy_score(y_test, y_pred)
print("Accuracy:", acc)
# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)

# Optional: Heatmap
sns. heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()
