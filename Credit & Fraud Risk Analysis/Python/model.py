import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (accuracy_score,confusion_matrix,classification_report)
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("Dataset/cleaned_data.csv")

#1 Correlation Analysis
le = LabelEncoder()
df["Merchant Name"] = le.fit_transform(df["Merchant Name"])
df["State"] = le.fit_transform(df["State"])
df["Card Type"] = le.fit_transform(df["Card Type"])

corr = df.corr(numeric_only=True)
# Visualization
plt.figure(figsize=(8,6))
sns.heatmap(corr,annot=True)
plt.title("Correlation Matrix")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output/charts/Correlation_Analysis.png")
plt.show()

#2 Feature Selection
X = df[["Transaction Amount (INR)","Merchant Name","State","Card Type","Fraud Score"]]
y = df["IsFraud"]

#3 Train Test Split
X_train,X_test,y_train,y_test = train_test_split( X,y,test_size=0.2,random_state=42)

#4 Logistic Regression
lr = LogisticRegression()
lr.fit(X_train, y_train)
pred_lr = lr.predict(X_test)


#5 Logistic Regression Accuracy
print(accuracy_score(y_test,pred_lr))


#6 Confusion Matrix
cm = confusion_matrix(y_test,pred_lr)
print(cm)


#7 Classification Report
print(classification_report(y_test, pred_lr))

#8 Random Forest
rf = RandomForestClassifier(n_estimators=100,random_state=42)
rf.fit(X_train,y_train)

#9 Prediction
pred_rf = rf.predict(X_test)


#10 Accuracy
print(accuracy_score(y_test,pred_rf))


#11 Feature Importance
importance = pd.DataFrame({'Feature':X.columns,'Importance':rf.feature_importances_})
importance = importance.sort_values(by='Importance',ascending=False)
print(importance)

