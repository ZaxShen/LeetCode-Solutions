-- Last updated: 8/4/2025, 10:43:57 PM
# Write your MySQL query statement below

WITH RECURSIVE
income_per_month AS
	(
	SELECT
		account_id,
		DATE_FORMAT(day, '%Y%m') AS 'date',
		SUM(amount) AS amount
	FROM Transactions
	WHERE type = 'Creditor'
	GROUP BY account_id, date
	ORDER BY account_id, date
	),
# SELECT * FROM income_per_month;
exceed_table AS
	(
	SELECT
		i.account_id, i.date, i.amount,
        max_income,
        IF(amount > max_income, 1, 0) AS if_exceed
	FROM income_per_month i
	LEFT JOIN Accounts a ON i.account_id = a.account_id
	)
# SELECT * FROM exceed_table;
SELECT DISTINCT(e1.account_id)
FROM exceed_table e1
INNER JOIN exceed_table e2 ON e1.account_id = e2.account_id
	AND e1.date = e2.date - 1
WHERE e1.if_exceed + e2.if_exceed > 1;