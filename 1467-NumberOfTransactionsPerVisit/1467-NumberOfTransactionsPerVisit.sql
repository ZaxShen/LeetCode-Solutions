-- Last updated: 8/4/2025, 10:45:30 PM
/*Number of Transactions per Visit
- Visits PK: (user_id, visit_date)
- Transactions PK: NULL

- SOLUTION:
*/
WITH RECURSIVE 
transaction_visit AS
	(
	SELECT
		v.user_id,
		v.visit_date,
		COUNT(DISTINCT v.user_id) AS count_user_id, # the unique visit
		COUNT(t.amount) AS count_amount
	FROM Visits v
	LEFT JOIN Transactions t
		ON v.user_id = t.user_id
		AND v.visit_date = t.transaction_date
	GROUP BY v.user_id, v.visit_date
    ),
transactions_per_visit AS
	(
	SELECT
		count_amount AS transactions_count,
		SUM(count_user_id) AS visits_count
	FROM transaction_visit
	GROUP BY count_amount
    ),
full_transactions AS
	(
	SELECT 0 AS transactions_count
    UNION ALL
    SELECT transactions_count + 1
    from full_transactions
    WHERE transactions_count < (SELECT MAX(transactions_count) FROM transactions_per_visit)
	)
SELECT f.transactions_count, IFNULL(t.visits_count, 0) AS visits_count
FROM full_transactions f
LEFT JOIN transactions_per_visit t
	USING(transactions_count); 