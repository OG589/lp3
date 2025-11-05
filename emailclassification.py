import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix,ConfusionMatrixDisplay, precision_score, recall_score, accuracy_score
data = pd.read_csv(r"C:\Users\karti\Downloads\emails.csv")
data

data = data.drop('Email No.', axis=1)
data.shape
data.describe()

data['Prediction'].value_counts ()

X = data.drop('Prediction', axis = 1)
y = data['Prediction']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size =
0.20)
from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors = 2)
neigh.fit(X_train, y_train)
KNeighborsClassifier(n_neighbors=2)
y_pred = neigh.predict(X_test)
neigh.score(X_train, y_train)
neigh.score(X_test, y_test)
print("Confusion Matrix: ")
cm = confusion_matrix(y_test, y_pred)
cm

print("recall_score: ")
recall_score(y_test, y_pred)
print("Error: ")
1-accuracy_score(y_test, y_pred)

from sklearn.svm import SVC
SVM = SVC(gamma = 'auto')
SVM.fit(X_train, y_train)
SVC (gamma='auto' )
y_pred = SVC.predict(y_test)

SVM.score(X_train, y_train)
SVM.score(X_test, y_test)
print("Confusion Matrix: ")
cm = confusion_matrix(y_test, y_pred)
cm
mat = ConfusionMatrixDisplay(confusion_matrix = cm)
mat.plot()
plt.show()


print("accuracy_score: ")
accuracy_score(y_test, y_pred)
accuracy_score:
print("precision score: ")
precision_score(y_test, y_pred)

print(classification_report(y_test, y_pred))
