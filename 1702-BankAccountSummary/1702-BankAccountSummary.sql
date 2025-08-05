-- Last updated: 8/4/2025, 10:44:23 PM
# Write your MySQL query statement below

WITH RECURSIVE
CTE AS
	(
	SELECT paid_by AS user_id, (-amount) AS amount
	FROM Transactions
	UNION ALL
	SELECT paid_to AS user_id, amount AS amount
	FROM Transactions
    UNION ALL
    SELECT user_id, credit
    FROM Users
    ),
# SELECT * FROM CTE;
CTE1 AS
	(
	SELECT
		c.user_id, u.user_name, 
		SUM(amount) AS credit
	FROM CTE c
	INNER JOIN Users u ON c.user_id = u.user_id
	GROUP BY user_id, user_name
	)
SELECT *, IF(credit < 0, 'Yes', 'No') AS credit_limit_breached
FROM CTE1;