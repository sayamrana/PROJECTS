import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = pd.read_csv(
    "Dataset/cleaned_data.csv"
)

os.makedirs(
    "output/charts",
    exist_ok=True
)

# Fraud Distribution
print(df['IsFraud'].value_counts())

# Visualization
plt.figure(figsize=(6,4))
sns.countplot(x='IsFraud',data=df)
plt.title("Fraud vs Genuine")
plt.savefig("output/charts/fraud_distribution.png")
plt.show()


# Fraud Percentage
fraud_rate = (df['IsFraud'].sum()/len(df))*100
print(f"Fraud Percentage: {fraud_rate:.2f}%")


# Transaction Amount Distribution(Visualization)
plt.figure(figsize=(10,5))
sns.histplot(df['Transaction Amount (INR)'],bins=30,kde=True)
plt.title("Transaction Amount Distribution")
plt.savefig("output/charts/Fraud_Percentage.png")
plt.show()


# Fraud Amount Analysis
fraud_df = df[df['IsFraud']==1]
print(fraud_df['Transaction Amount (INR)'].describe())


# Fraud by State
fraud_state = df.groupby('State')['IsFraud'].sum()
fraud_state = fraud_state.sort_values( ascending=False)
print(fraud_state)
# Visualization
plt.figure(figsize=(10,5))
fraud_state.plot(kind='bar')
plt.title("Fraud Cases by State")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output/charts/Fraud_by_State.png")
plt.show()


# Fraud by Card Type
card_fraud = df.groupby('Card Type')['IsFraud'].sum()
print(card_fraud)
# Visualization
card_fraud.plot(kind='bar')
plt.title("Fraud by Card Type")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output/charts/Fraud_by_Card_Type.png")
plt.show()



# Fraud by Merchant
merchant_fraud = df.groupby('Merchant Name')['IsFraud'].sum()
merchant_fraud = merchant_fraud.sort_values(ascending=False)
print(merchant_fraud.head(10))
# Visualization
merchant_fraud.head(10).plot(kind='bar')
plt.title("Top Fraud Merchants")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output/charts/Fraud_by_Merchant.png")
plt.show()



# Top Risky States
top_states = df.groupby('State')['Fraud Score'].mean().reset_index()
top_states = top_states.sort_values(by='Fraud Score',ascending=False)

print(top_states)
# Visualization
plt.figure(figsize=(12,6))
sns.barplot(data=top_states,x='State',y='Fraud Score')
plt.title('Average Fraud Score by State')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output/charts/Top_Risky_States.png")
plt.show()