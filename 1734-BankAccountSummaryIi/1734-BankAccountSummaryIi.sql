-- Last updated: 8/4/2025, 10:44:22 PM
# Write your MySQL query statement below

SELECT
	name,
    SUM(amount) AS balance
FROM Users u
LEFT JOIN Transactions t ON u.account = t.account
GROUP BY name
HAVING balance > 10000;