CREATE DATABASE ecommerce;
USE ecommerce;

SHOW TABLES;
DESCRIBE Superstore;

SELECT COUNT(*) AS total_rows
FROM superstore;
SHOW WARNINGS;

SELECT COUNT(*) FROM superstore;

DESCRIBE superstore;

DROP TABLE IF EXISTS superstore;

CREATE TABLE superstore (
    `Row ID` INT,
    `Order ID` VARCHAR(30),
    `Order Date` DATE,
    `Ship Date` DATE,
    `Ship Mode` VARCHAR(50),
    `Customer ID` VARCHAR(30),
    `Customer Name` VARCHAR(100),
    `Segment` VARCHAR(30),
    `Country` VARCHAR(50),
    `City` VARCHAR(50),
    `State` VARCHAR(50),
    `Postal Code` VARCHAR(20),
    `Region` VARCHAR(30),
    `Product ID` VARCHAR(50),
    `Category` VARCHAR(50),
    `Sub-Category` VARCHAR(50),
    `Product Name` TEXT,
    `Sales` DECIMAL(10,2),
    `Quantity` INT,
    `Discount` DECIMAL(4,2),
    `Profit` DECIMAL(10,4)
);

LOAD DATA LOCAL INFILE 'D:\PROJECTS/Superstore.csv'
INTO TABLE superstore
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

SELECT COUNT(*) AS Total_Records
FROM superstore;

SELECT * FROM superstore LIMIT 5;



SELECT ROUND(SUM(Sales), 2) AS TotalRevenue
FROM superstore;

SELECT COUNT(`Order ID`) AS TotalOrders
FROM superstore;

SELECT `Product Name`, ROUND(SUM(Sales),2) AS Revenue
FROM superstore
GROUP BY `Product Name`
ORDER BY Revenue DESC
LIMIT 10;

SELECT State,
ROUND(SUM(Sales),2) AS Revenue
FROM Superstore
GROUP BY State
ORDER BY Revenue DESC;


SELECT `Customer Name`,
ROUND(SUM(Sales),2) AS Spending
FROM Superstore
GROUP BY `Customer Name`
ORDER BY Spending DESC;


SELECT
MONTH('Order Date') AS Month,
SUM(Sales) AS Revenue
FROM Superstore
GROUP BY Month;

SELECT
  MONTH(`Order Date`) AS Month,
  SUM(Sales) AS Revenue
FROM Superstore
WHERE `Order Date` IS NOT NULL
GROUP BY MONTH(`Order Date`);