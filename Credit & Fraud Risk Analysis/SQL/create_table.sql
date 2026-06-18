CREATE DATABASE FraudAnalysis;

USE FraudAnalysis;

CREATE TABLE Transactions
(
Transaction_ID BIGINT,
Customer_Name VARCHAR(100),
Transaction_Amount DECIMAL(10,2),
Merchant VARCHAR(100),
State VARCHAR(50),
Card_Type VARCHAR(50),
IsFraud INT,
Fraud_Score INT
);


-- Total Transactions
SELECT COUNT(*) AS Total_Transactions FROM Transactions;

-- Total Fraud Cases
SELECT COUNT(*) AS Fraud_Cases FROM Transactions WHERE IsFraud=1;

-- Fraud Percentage
SELECT ROUND(SUM(IsFraud)*100.0/COUNT(*),2) AS Fraud_PercentageFROM Transactions;

-- Fraud by State
SELECT State,SUM(IsFraud) AS Fraud_Count FROM Transactions GROUP BY State ORDER BY Fraud_Count DESC;

-- Fraud by Card Type
SELECT Card_Type,SUM(IsFraud) AS Fraud_Count FROM Transactions GROUP BY Card_Type ORDER BY Fraud_Count DESC;

-- Fraud by Merchant
SELECT Merchant, SUM(IsFraud) AS Fraud_Count FROM Transactions GROUP BY Merchant ORDER BY Fraud_Count DESC;

-- Top 10 Fraud Customers
SELECT Customer_ID, COUNT(*) AS Fraud_Transactions FROM Transactions WHERE IsFraud=1 GROUP BY Customer_ID ORDER BY Fraud_Transactions DESC LIMIT 10;

-- Average Fraud Amount
SELECT AVG(Amount) FROM Transactions WHERE IsFraud=1;

-- Maximum Fraud Amount
SELECT MAX(Amount) FROM Transactions WHERE IsFraud=1;

-- Minimum Fraud Amount
SELECT MIN(Amount) FROM Transactions WHERE IsFraud=1;

-- High Risk Transactions
SELECT * FROM Transactions WHERE Fraud_Score > 80;